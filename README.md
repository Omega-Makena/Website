# Personal Website Template

A professional personal website built with Flask, Jinja2, and TailwindCSS. Features a portfolio, multi-category blog, dark mode, and static site generation for deployment to GitHub Pages.

## Features

- Clean, modern design with dark mode support
- Responsive mobile-first layout
- Markdown-based blog with category organization
- Folder-based portfolio structure
- Zero-code content management
- Static site generation for GitHub Pages

## Quick Start

### Install Dependencies

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Configure Your Site

Edit `config.yaml` to add your personal information:

```yaml
site:
  title: Your Name
  tagline: Your Professional Title
  url: https://yourusername.github.io/website

personal:
  name: Your Name
  email: your@email.com
  bio: |
    <p>Your bio here...</p>

social:
  github: https://github.com/yourusername
  linkedin: https://linkedin.com/in/yourusername
  email: your@email.com
```

### Add Your Content

**Add Blog Posts:** Create markdown files in `blog/category/filename.md`

```markdown
---
title: Post Title
date: 2025-01-15
category: ai-ml
description: Brief description
---

Your post content here...
```

**Add Portfolio Projects:** Create folders in `portfolio/projects/project-name/` with an `index.md` file

```markdown
---
title: Project Name
description: What it does
tech:
  - Python
  - JavaScript
github_url: https://github.com/you/project
---

Project details here...
```

**Available blog categories:** `ai-ml`, `finance-economics`, `poetry`, `self-improvement`, `tech-concepts`, `random`

### Run Locally

```bash
python app.py
```

Visit `http://localhost:5000` to preview your site.

## Deployment to GitHub Pages

1. **Generate static site:**
```bash
python freeze.py
```

2. **Configure GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Branch `main`, Folder `/docs`

3. **Push to GitHub:**
```bash
git add .
git commit -m "Deploy website"
git push origin main
```

Your site will be live at `https://yourusername.github.io/website`

### Custom Domain (Optional)

Add a `CNAME` file with your domain, then configure DNS with GitHub Pages IP addresses.

## Project Structure

```
.
├── app.py              # Flask application
├── freeze.py          # Static site generator
├── config.yaml        # Site configuration
├── templates/         # HTML templates
├── blog/              # Blog posts by category
├── portfolio/         # Portfolio projects
├── static/            # CSS, images, etc.
└── docs/              # Generated static site (git push this)
```

## Technologies

- Flask + Flask-FlatPages (markdown blog)
- Frozen-Flask (static site generation)
- TailwindCSS (styling)
- Jinja2 (templating)

## Contributing

Issues and pull requests welcome!

## License

Free to use for personal websites.

## Contact

Edit your contact information in `config.yaml` and update this section in the README.

---

*Template for building static personal websites with Flask*
