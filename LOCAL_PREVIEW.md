# Preview the production AI redesign

Development branch: `codex/homepage-resume-alignment`.

## Native Jekyll preview

On this Apple Silicon Mac, install a separate Homebrew Ruby and ImageMagick.
The macOS system Ruby 2.6 cannot install the project's current dependencies.
If Homebrew reports an unaccepted Xcode license, first run
`sudo xcodebuild -license` in Terminal, review the agreement, and accept it if
you agree. This requires your administrator password.

```sh
brew install ruby@3.3 imagemagick
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
hash -r
ruby --version
bundle --version
```

Confirm Ruby reports **3.3.x**, then run the following from the repository root.
Repeat the `export PATH` command in each new terminal session before running
Bundler; it selects Homebrew Ruby without changing Apple's system Ruby.
Port 4001 and the separate build directory avoid colliding with an existing
preview on port 4000.

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4001 --destination /tmp/omkar-home-resume-review
```

Open <http://127.0.0.1:4001>. Stop the server with Ctrl+C. Restart it after
editing `_config.yml`.

For a production build:

```sh
JEKYLL_ENV=production bundle exec jekyll build --lsi
```

The existing container alternative is `docker compose up`, which exposes the
site at <http://localhost:8080>. It requires a working Docker engine and downloads
the al-folio image on first use.

## Review checklist

- Check Home, Projects, Resume, and Publications on desktop and mobile.
- Switch between light and dark themes and use the keyboard to navigate.
- Follow the selected work links to their sections on Projects.
- Confirm all three Earlier Work links still open their original project URLs.
- Confirm the canonical URL and Open Graph URLs use `https://omkarchittar.com`.
- Confirm the published PDF matches `resume_SWE.pdf`, and the old resume JSON and theme demo posts are absent from `_site`.

The Resume navigation item keeps the existing `/cv/` URL. Its text comes from
`assets/json/resume.json`, synchronized with the latest supplied `resume_SWE.pdf`.
The PDF is copied unchanged to `assets/pdf/resume.pdf`, which is linked from the
Resume page. The homepage Resume CTA opens the web resume. The root source PDF is excluded from publication to
avoid publishing duplicate copies. Contact email is `ochittar@gmail.com`.

Selected Work summaries are shared between the homepage and Projects through
`_data/selected_work.yml`. Four featured summaries appear on Home and Projects, including LLM
evaluation and serving. Claims use only information in
the supplied resume. Earlier robotics and computer vision project URLs remain
unchanged.

`CNAME` and site metadata use `omkarchittar.com`. DNS and GitHub Pages settings
were not changed; this branch does not deploy automatically when pushed.

## Homepage and resume alignment review

The live-site audit found the production AI homepage and current employment
history already published. This branch completes the hero links, aligns SEO
and social titles, and improves the web resume's hierarchy and rendering.
The source PDF and role accomplishments are unchanged. Missing dates for Sai
Classes and the University of Maryland transportation role remain omitted;
confirm those dates before adding them. No additional public AI case study
exists in the current source content to add beyond the shared Selected Work.

The resume shows Work Experience, Skills, Education, and Teaching & Community.
Contact links are in its header. Robotics experience remains under Earlier Work.
Summary arrays render as bullets; text summaries render as paragraphs.
The unused `assets/json/resume_og.json` has been removed. Demo posts and news
remain excluded from publication. Deployment workflows and domain settings
are unchanged. The homepage and resume alignment changes were reviewed and
approved for publication.
