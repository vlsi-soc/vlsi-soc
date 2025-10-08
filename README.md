# VLSI-SoC 2026 Conference Website

Official website for the 34th IFIP/IEEE International Conference on Very Large Scale Integration, October 11-14, 2026, Limassol, Cyprus.

## Quick Start

```bash
# Install dependencies
bundle install

# Run development server
bundle exec jekyll serve
```

Open browser to `http://localhost:4000`

## Project Structure

```
├── _config.yml                 # Site configuration
├── _data/                      # Data files (YAML)
│   ├── carousel.yml
│   ├── contacts.yml
│   ├── organizing_committee.yml
│   ├── program_committee.yml
│   ├── sponsors.yml
│   └── steering_committee.yml
├── _includes/                  # Reusable components
│   ├── footer.html
│   ├── head.html
│   ├── hero-carousel.html
│   ├── logo-bar.html
│   ├── navigation.html
│   └── organizing_committee.html
├── _layouts/
│   └── default.html
├── css/, js/, img/, docs/      # Assets
├── *.md                        # Pages (index, committee, etc.)
└── _site/                      # Generated site (git ignored)
```

## Updating Content

### Committee Information
Edit `_data/organizing_committee.yml` - changes appear on all relevant pages

### Contacts  
Edit `_data/contacts.yml` - updates footer on all pages

### Sponsors
Edit `_data/sponsors.yml` - updates logo bar and footer

### Pages
Edit the respective `.md` files - use YAML front matter for metadata

## Building & Deployment

```bash
# Build for production
bundle exec jekyll build

# Output in _site/ directory
```

**Deploy to:** GitHub Pages, Netlify, Vercel, or any static host

## Key Features

- **Data-driven**: All content in `_data/` YAML files (no duplication)
- **Modular**: Reusable components in `_includes/`
- **Clean**: 87% code reduction through refactoring (199 → 25 lines for committees)

## Technologies

Jekyll 4.3, Bootstrap 4, Font Awesome, WOW.js, Particles.js
