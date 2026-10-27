# VLSI-SoC Conference Website

Official website of the IFIP/IEEE International Conference on Very Large Scale Integration SoC (VLSI-SoC), served at https://vlsi-soc.com.

Past editions are archived as static snapshots under `/<year>/` (e.g. `2026/` → https://vlsi-soc.com/2026/).

## Quick Start for local setup

```bash
# Install dependencies
bundle install

# Run development server
bundle exec jekyll serve
```

Open browser to `http://localhost:4000`

## Updating Content

For updating the contents without modifying the site style, just edit the YAML data files in `_data`.

General conference information (name, edition, location, dates) is in `_data/conference.yml`.
Set `show_full_nav: true` there, and remove `published: false` from the edition-specific pages
(`submission.md`, `specialsession.md`, `phd.md`, `program.md`, `registration.md`, `travel.md`, `sponsorship.md`),
once they have content for the new edition.

The hero carousel is configured in `_data/carousel.yml`.

While for editing the styles or the pages' structure, edit the respective `.md` files - use YAML front matter for metadata.

## Building & Deployment

```bash
# Build for production
bundle exec jekyll build

# Output in _site/ directory
```

Pushing to `main` deploys the site to GitHub Pages via `.github/workflows/jekyll.yml`.

## Archiving a past edition

Once a conference is over, freeze its website under `/<year>/` before preparing the next edition:

```bash
YEAR=2026
git tag vlsi-soc-$YEAR
JEKYLL_ENV=production bundle exec jekyll build \
  --config _config.yml,_config_archive.yml --baseurl /$YEAR -d /tmp/$YEAR
rm -rf /tmp/$YEAR/{CNAME,robots.txt,sitemap.xml,scripts}
cp -r /tmp/$YEAR ./$YEAR
```

`_config_archive.yml` enables a banner pointing visitors to the current conference.
The generated files have no front matter, so Jekyll copies the `<year>/` folder verbatim.
Then link the archive from `_data/previous_conferences.yml` (`url: "/<year>/"`) and reset the
`_data` files for the next edition. The full source of each edition stays available at its `vlsi-soc-<year>` tag.
