"""Validate gallery structure, semantic captions, and original media coverage."""
from pathlib import Path
from html.parser import HTMLParser
import re, sys
build=Path(sys.argv[1])
source=Path(__file__).resolve().parents[1]
expected_counts={'1_project':17,'2_project':9,'3_project':8}
class Gallery(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images=[];self.captions=0;self.h1=0;self.nested_link=False;self.in_link=False
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='a':
            assert not self.in_link,'Nested link'
            self.in_link=True
        if tag=='img':self.images.append(attrs)
        if tag=='figcaption':self.captions+=1
        if tag=='h1':self.h1+=1
    def handle_endtag(self,tag):
        if tag=='a':self.in_link=False
for slug,count in expected_counts.items():
    html=(build/'projects'/slug/'index.html').read_text()
    assert 'project-detail' in html,f'Missing shared gallery layout: {slug}'
    assert 'gallery-grid' in html,f'Missing image grid: {slug}'
    assert not re.search(r'class="[^"]*\brow\b',html),'Remove nested Bootstrap rows from gallery content'
    page=Gallery();page.feed(html)
    assert page.h1==1,(slug,page.h1)
    assert len(page.images)==count,(slug,len(page.images),count)
    assert page.captions==count,(slug,page.captions,count)
    original=re.findall(r'path="([^"]+)"',(source/'_projects'/(slug+'.md')).read_text())
    assert sorted(img['src'].lstrip('/') for img in page.images)==sorted(original)
    for img in page.images:
        assert img.get('alt','').strip(),f'Missing image description: {slug}'
        assert (build/img['src'].lstrip('/')).is_file(),img['src']
print('Passed: all three internal galleries use aligned figures, captions and one page heading; original images and GIFs are present.')
