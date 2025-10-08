# VLSI-SoC 2026 Conference Website

This is the official website for the VLSI-SoC 2026 conference, built with Jekyll.

## Prerequisites

- Ruby (version 2.7 or higher)
- Bundler gem

## Setup

1. Install Ruby dependencies:
```bash
bundle install
```

2. Run the development server:
```bash
bundle exec jekyll serve
```

3. Open your browser and navigate to `http://localhost:4000`

## Building for Production

To build the static site for production:

```bash
bundle exec jekyll build
```

The generated site will be in the `_site` directory.

## Project Structure

```
.
├── _config.yml                 # Jekyll configuration
├── _data/                      # Data files (YAML)
│   ├── organizing_committee.yml
│   ├── program_committee.yml
│   ├── steering_committee.yml
│   └── carousel.yml
├── _includes/                  # Reusable components
│   ├── head.html
│   ├── navigation.html
│   ├── footer.html
│   ├── logo-bar.html
│   ├── hero-carousel.html
│   └── organizing_committee.html
├── _layouts/                   # Page layouts
│   └── default.html
├── css/                        # Stylesheets
├── img/                        # Images
├── js/                         # JavaScript files
├── docs/                       # PDF documents
├── index.md                    # Homepage
├── committee.md                # Committee page
└── [other pages].html          # Other pages to be converted
```

## Key Features

### De-duplication
- Committee data is stored once in `_data/` YAML files
- Reusable components are in `_includes/`
- Common layout structure in `_layouts/default.html`
- No more repeated HTML code across pages

### Data Files
- `organizing_committee.yml` - All organizing committee members
- `program_committee.yml` - Program committee organized by tracks
- `steering_committee.yml` - Steering committee members
- `carousel.yml` - Carousel images configuration

### Includes (Reusable Components)
- `head.html` - HTML head with meta tags and CSS
- `navigation.html` - Site navigation menu
- `footer.html` - Site footer with scripts
- `logo-bar.html` - Sponsor logos bar
- `hero-carousel.html` - Hero section with carousel
- `organizing_committee.html` - Organizing committee section (reusable across pages)

## Converting Remaining Pages

To convert other HTML pages to Jekyll:

1. Rename `.html` to `.md` (or keep as `.html`)
2. Add front matter at the top:
```yaml
---
layout: default
title: "Page Title"
description: "Page description"
---
```
3. Remove the `<head>`, navigation, footer, and other duplicated sections
4. Keep only the main content
5. Update image/CSS paths to use `{{ '/path/to/file' | relative_url }}`

## Updating Committee Information

Simply edit the YAML files in `_data/`:
- Changes will automatically reflect on all pages using that data
- No need to update multiple HTML files

## Deployment

The site can be deployed to:
- GitHub Pages
- Netlify
- Vercel
- Any static hosting service

For GitHub Pages, push to the `main` branch and enable Pages in repository settings.
