# VLSI-SoC 2026 Conference Website

Official website for the 35th IFIP/IEEE International Conference on Very Large Scale Integration SoC, October 11-14, 2026, Limassol, Cyprus.

## Quick Start for local setup

```bash
# Install dependencies
bundle install

# Run development server
bundle exec jekyll serve
```

Open browser to `http://localhost:4000/vlsi-soc`

## Updating Content

For updating the contents without modifying the site style, just edit the YAML data files in `_data`.

While for editing the styles or the pages' structure, edit the respective `.md` files - use YAML front matter for metadata.

## Building & Deployment

```bash
# Build for production
bundle exec jekyll build

# Output in _site/ directory
```
