from pathlib import Path
import re, sys
build=Path(sys.argv[1])
expected={
 'estimating-platform': ['DOCUMENT', 'GEOMETRY'],
 'speech-pipelines': ['AUDIO', 'SPEAKER A', 'SPEAKER B'],
 'llm-evaluation': ['QUERY SET', 'TOP-5 RETRIEVAL', 'CACHE / ROUTE'],
 'ci-debugging': ['FAILED BUILD', 'SUGGESTED FIX'],
 'media-pipelines': ['VIDEO CLIPS', 'VECTOR INDEX', 'SEARCH RESULTS'],
 'knowledge-discovery': ['DOCUMENT', 'VERIFIED', 'RETRIEVE / CHECK / CITE'],
 'operational-agents': ['DETECT', 'SURFACE', 'RESOLVE'],
}
for route,keys in [('',[key for key in expected if key not in ['speech-pipelines', 'llm-evaluation']]),('projects',list(expected))]:
 html=(build/route/'index.html').read_text()
 articles=re.findall(r'<article\b[^>]*>.*?</article>',html,re.S)
 for key in keys:
  card=next((a for a in articles if f'id="{key}"' in a or f'#{key}"' in a),None)
  assert card, f'Missing project card: {route}/{key}'
  assert f'data-project-art="{key}"' in card, f'Artwork not paired with {route}/{key}'
  assert 'role="img"' in card and 'aria-label=' in card, f'Missing visual description: {key}'
  for label in expected[key]: assert label in card, f'Missing visual concept {label}: {key}'
print('Passed: all seven professional cards have matching artwork; all five homepage projects retain their visuals.')
