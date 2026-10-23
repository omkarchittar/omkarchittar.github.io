"""Keep the original project collection discoverable on the Projects page."""
from pathlib import Path
from html.parser import HTMLParser
import re
import sys

source = Path(__file__).resolve().parents[1]
build = Path(sys.argv[1])
html = (build / 'projects/index.html').read_text()

class LinksAndImages(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.images, self.thumbnails = set(), set(), set()
        self.current_link = None
        self.current_thumbnail = None
        self.thumbnail_shapes = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a':
            self.current_link = attrs.get('href', '')
            self.links.add(self.current_link)
        if tag == 'svg' and 'data-repository-thumbnail' in attrs:
            repo = attrs['data-repository-thumbnail']
            assert self.current_link == 'https://github.com/' + repo, f'Thumbnail paired with wrong project: {repo}'
            self.thumbnails.add(repo)
            self.current_thumbnail = repo
            self.thumbnail_shapes = 0
        if self.current_thumbnail and tag in ["path", "circle", "polygon", "polyline"]:
            self.thumbnail_shapes += 1
        if tag == 'img':
            self.images.add(attrs.get('src', ''))

    def handle_endtag(self, tag):
        if tag == 'svg' and self.current_thumbnail:
            assert self.thumbnail_shapes, f'Empty thumbnail: {self.current_thumbnail}'
            self.current_thumbnail = None
        if tag == 'a':
            self.current_link = None

page = LinksAndImages()
page.feed(html)
repos = set(re.findall(r'^  - (omkarchittar/[\w-]+)', (source / '_data/repositories.yml').read_text(), re.M))
for path in (source / '_projects').glob('*.md'):
    content = path.read_text()
    repos.update(re.findall(r'https://github.com/(omkarchittar/[\w-]+)', content))
    assert f'/projects/{path.stem}/' in page.links, f'Missing original gallery: {path.stem}'
    cards = re.findall(r'<article\b[^>]*>.*?</article>', html, re.S)
    card = next(card for card in cards if f'/projects/{path.stem}/' in card)
    assert f'data-gallery-art="{path.stem}"' in card, f'Missing themed gallery thumbnail: {path.stem}'
    assert '<svg' in card and 'role="img"' in card, f'Missing accessible gallery illustration: {path.stem}'
for repo in repos:
    assert 'https://github.com/' + repo in page.links, f'Project absent from index: {repo}'
    assert repo in page.thumbnails, f'Missing small project thumbnail: {repo}'
assert html.index('id="earlier-work"') < html.index('id="production-work-title"'), 'Original galleries should be visible before long case studies'
assert 'id="project-index"' in html
print(f'Passed: original galleries retained with themed thumbnails; all {len(repos)} project repositories have matching small thumbnails.')
