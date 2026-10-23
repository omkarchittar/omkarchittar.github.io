"""Check the built website: python3 tests/site.test.py /path/to/jekyll-output."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import sys

build = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
source = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.images, self.h1 = set(), [], [], 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "img":
            self.images.append(attrs)


def read_page(path):
    assert path.is_file(), f"Missing page: {path}"
    page = Page()
    page.feed(path.read_text())
    return page


primary = ["", "projects", "cv", "publications", "teaching", "repositories"]
legacy = ["projects/1_project", "projects/2_project", "projects/3_project"]
for route in primary + legacy:
    path = build / route / "index.html"
    page = read_page(path)
    if route in primary:
        assert page.h1 == 1, (route, page.h1)
    for href in page.links:
        url = urlparse(href)
        if url.scheme or url.netloc or not url.path.startswith("/"):
            continue
        target = build / unquote(url.path.lstrip("/"))
        if url.path.endswith("/"):
            target /= "index.html"
        assert target.is_file(), (route, href)
        if url.fragment and target.suffix == ".html":
            assert unquote(url.fragment) in read_page(target).ids, (route, href)

home = read_page(build / "index.html")
assert any(img.get("alt") == "Portrait of Omkar Chittar" for img in home.images)
assert (build / "assets/img/omkar-chittar.jpg").is_file()
assert (source / "assets/pdf/resume.pdf").read_bytes() == (build / "assets/pdf/resume.pdf").read_bytes()
assert not (build / "tests").exists(), "Tests must not be published"
assert not (build / "resume_SWE.pdf").exists(), "Do not publish the old source resume"

resume = json.loads((source / "assets/json/resume.json").read_text())
assert resume["basics"]["label"] == "Software Engineer"
assert len(resume["work"][0]["summary"]) == 7
assert len(resume["work"][1]["summary"]) == 8
assert resume["work"][1]["position"] == "AI Engineer", "Keep actual historical role titles"
assert len(resume["publications"]) == 2
rendered_resume = (build / "cv/index.html").read_text()
for text in ["FastAPI", "GitHub Actions", "Kubernetes", "gRPC", "TimeSformer", "Redis", "warehouse data modeling"]:
    assert text in rendered_resume, f"Missing new resume detail: {text}"
assert "Software Engineer &amp; AI Engineer" not in (build / "index.html").read_text()
print("Passed: primary pages, legacy routes, internal links, portrait, PDF, new resume details, and publication exclusions.")
