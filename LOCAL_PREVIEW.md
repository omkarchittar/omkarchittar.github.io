# Editorial software portfolio

This redesign applies the selected warm editorial layout to the existing Jekyll site. The homepage uses an abstract mathematical point cloud, a small About portrait, and conceptual project illustrations. The existing theme control switches between warm light and dark palettes and remembers the visitor's choice.

## Current resume

The authoritative source is `Omkar_swe.pdf`, supplied on October 22, 2026. Its bytes are copied unchanged to `assets/pdf/resume.pdf`. Web experience and skills are in `assets/json/resume.json`; `_data/cv.yml` retains the synchronized fallback. Historical job titles, education, dates, and accomplishments are preserved. The site's overall positioning is Software Engineer.

New work includes the CI debugging agent, video understanding pipelines, speech transcription and diarization, and Apache Airflow orchestration. Shared project descriptions and conceptual pipeline steps live in `_data/selected_work.yml`. The homepage features five projects; Projects preserves all existing anchors and includes the additional work.

## Build and preview

Use the existing Homebrew Ruby 3.3 installation and installed gems:

```sh
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
bundle check
bundle exec jekyll serve --host 127.0.0.1 --port 4001 --destination /tmp/omkar-editorial-preview
```

Open <http://127.0.0.1:4001>. Stop with Ctrl+C. Restart after changing `_config.yml`.

```sh
node tests/point-cloud.test.cjs
bundle exec jekyll build --destination /tmp/omkar-editorial-build
python3 tests/site.test.py /tmp/omkar-editorial-build
python3 tests/visual-pairings.test.py /tmp/omkar-editorial-build
python3 tests/project-collection.test.py /tmp/omkar-editorial-build
python3 tests/internal-galleries.test.py /tmp/omkar-editorial-build
```

## Check before publication

- Test Home, Projects, Resume, Publications, and older project URLs on desktop and mobile.
- Switch themes, navigate to another page, and confirm the chosen theme persists.
- Confirm the About portrait loads and the resume download opens the current PDF.
- Operate the point-cloud slider with the keyboard; pause/resume motion and check reduced-motion behavior.
- Diagrams illustrate the published project descriptions; they are not actual product screenshots.

No domain, deployment workflow, or access settings were changed. Pushing to master/main invokes the existing deployment workflow; review changes before publishing. The user's root `image.png` and `resume_SWE.pdf` are untouched.

Projects presents the three original galleries, a complete index of all 28 repositories referenced by the galleries or repository data, and the seven professional case studies. Gallery contents and legacy URLs are preserved.

All seven professional projects have matching artwork. Gallery thumbnails use themed vector diagrams; the original gallery images and animations remain in the detail pages. The estimating plan illustration is shared between Home and Projects.

The All projects index includes 28 compact, project-specific vector thumbnails. Each remains inside its corresponding repository link and follows the light/dark palette.

The three internal gallery pages use one responsive figure/caption layout, retaining all 34 original media files and project links. Scoped print rules remove Bootstrap's fixed-width body/container and A3 page setting.
