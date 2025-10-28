# Omega Makena - Personal Website

A professional personal website built with **Flask + Jinja2** and **TailwindCSS**, featuring a portfolio, multi-category blog, and dark mode toggle. Designed for deployment to **GitHub Pages**.

## Features

- **Modern Design**: Clean, academic-modern aesthetic with custom color palette
- **Dark Mode**: Seamless light/dark theme toggle with localStorage persistence (defaults to dark mode)
- **Responsive**: Mobile-first design that works on all devices
- **Dynamic Content Management**: Add blog posts and portfolio projects without editing code
- **Blog System**: Markdown-based blog with category organization
- **Portfolio**: Showcase projects with folder-based structure
- **SEO Optimized**: Meta tags, Open Graph, and social card support
- **Static Site Generation**: Converts Flask app to static HTML for GitHub Pages

## Project Structure

```
.
├── app.py                      # Flask application
├── freeze.py                   # Static site generator
├── requirements.txt            # Python dependencies
├── config.yaml                 # Site configuration (personal info, social links)
├── CNAME                       # Custom domain configuration
├── templates/                  # Jinja2 templates
│   ├── base.html              # Base template with navbar/footer
│   ├── index.html             # Home/About page
│   ├── portfolio.html         # Portfolio projects listing
│   ├── project.html           # Individual project detail page
│   ├── blog.html              # Blog categories page
│   ├── blog_category.html     # Individual category page
│   └── post.html              # Individual blog post page
├── portfolio/                  # Portfolio projects
│   └── projects/              # Individual project folders
│       ├── online-learning/   # Each project has its own folder
│       │   ├── index.md       # Project metadata and content
│       │   └── assets/        # Project-specific images/files
│       ├── scarcity/
│       ├── sarima/
│       ├── anomaly-detection/
│       └── quant-model/
├── blog/                       # Blog posts organized by category
│   ├── ai-ml/                 # AI & Machine Learning
│   ├── finance-economics/     # Finance & Economics
│   ├── poetry/                # Poetry
│   ├── self-improvement/      # Self-Improvement
│   ├── tech-concepts/         # Tech Concepts
│   └── random/                # Random Thoughts
├── static/                     # Static assets
│   └── img/                   # Images (profile, favicon, etc.)
└── docs/                      # Generated static site (for GitHub Pages)
```

## Quick Start

### Prerequisites

- **Python 3.8+**
- **Git**

### 1. Clone the Repository

```bash
git clone https://github.com/Omega-Makena/Website.git
cd Website
```

### 2. Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 3. Customize Your Site

Edit `config.yaml` to update your personal information, social links, and site settings.

### 4. Run Development Server

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## Content Management

### Update Personal Information

Edit `config.yaml`:

```yaml
site:
  title: Your Name
  tagline: Your Professional Title
  description: Your site description
  url: https://yourwebsite.com

personal:
  name: Your Name
  email: your@email.com
  location: Your Location
  bio: |
    <p>Your professional bio here...</p>
  profile_image: profile.jpg

social:
  github: https://github.com/yourusername
  linkedin: https://linkedin.com/in/yourusername
  email: your@email.com
```

### Add Portfolio Projects

Create a folder in `portfolio/projects/` with your project name, then create an `index.md` file:

**File:** `portfolio/projects/my-project/index.md`

```markdown
---
title: My Amazing Project
description: What your project does and why it's awesome
tech:
  - Python
  - React
  - PostgreSQL
live_url: https://myproject.com
github_url: https://github.com/yourusername/project
image: project-screenshot.jpg
order: 1
featured: true
---

# Project Details

Write your project description, features, and details here in Markdown.

Add images by placing them in the same folder and referencing them:

![Project Screenshot](project-screenshot.jpg)
```

### Add Blog Posts

Create markdown files in the appropriate category folder under `blog/`:

**File:** `blog/ai-ml/my-post.md`

```markdown
---
title: Your Post Title
date: 2025-11-29
category: ai-ml
author: Omega Makena
description: A brief description of your post
---

# Your Content Here

Write your blog post content in Markdown...

## Section Header

Content here with proper Markdown formatting.
```

**Available Blog Categories:**
- `ai-ml` - AI & Machine Learning
- `finance-economics` - Finance & Economics
- `poetry` - Poetry
- `self-improvement` - Self-Improvement
- `tech-concepts` - Tech Concepts
- `random` - Random Thoughts

### Add Images

Place images in `static/img/`:
- `profile.jpg` - Your professional photo
- `favicon.ico` - Browser favicon
- `apple-touch-icon.png` - iOS home screen icon
- `social-card.jpg` - Open Graph preview image (1200x630px)

## Deployment to GitHub Pages

### Step 1: Generate Static Site

```bash
python freeze.py
```

This creates a `docs/` folder with static HTML files and copies the `CNAME` file for custom domain support.

### Step 2: Configure GitHub Repository

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select:
   - Branch: `main`
   - Folder: `/docs`
4. Click **Save**

### Step 3: Configure Custom Domain (Optional)

The `CNAME` file is configured with `omegamakena.co.ke`.

**DNS Configuration** (at your domain registrar):

Add these **A Records**:
```
Host: @
Value: 185.199.108.153
Value: 185.199.109.153
Value: 185.199.110.153
Value: 185.199.111.153
```

Optionally add **CNAME Record**:
```
Host: www
Value: omega-makena.github.io
```

### Step 4: Push to GitHub

```bash
# Generate static files
python freeze.py

# Add and commit
git add .
git commit -m "Update website"
git push origin main
```

### Step 5: Enable HTTPS

In GitHub Pages settings, check **Enforce HTTPS** (available after DNS propagates, typically 24-48 hours).

## Development Workflow

### Local Development

```bash
# Run Flask dev server with auto-reload
python app.py

# Make changes to templates, portfolio projects, or blog posts
# Refresh browser to see changes (auto-reload enabled)
```

### Build and Deploy

```bash
# 1. Generate static site
python freeze.py

# 2. Test locally
cd docs
python -m http.server 8000
# Visit http://localhost:8000

# 3. Deploy to GitHub
git add .
git commit -m "Update website"
git push origin main
```

## Technologies Used

- **Flask** - Web framework
- **Flask-FlatPages** - Markdown blog posts
- **Frozen-Flask** - Static site generation
- **TailwindCSS** - Styling (CDN version)
- **Jinja2** - Templating
- **Markdown** - Blog content format
- **PyYAML** - Configuration and frontmatter parsing
- **Python-Frontmatter** - Frontmatter extraction

## Current Implementation

### Portfolio Projects

The website currently showcases 5 portfolio projects:
1. **Online Learning System** - An adaptive e-learning platform
2. **SCARCITY** - Economic resource scarcity simulation
3. **SARIMA Model** - Time series forecasting for economic data
4. **Anomaly Detection** - ML-based system for detecting unusual patterns
5. **Quantitative Model** - Financial risk and return modeling

Each project has its own dedicated page with detailed descriptions, tech stack, and related assets.

### Blog System

The blog features a category-based organization with collapsible sections. Current categories include:
- **AI & Machine Learning** - Articles on meta-learning, federated learning, AI architectures, and research
- **Finance & Economics** - Analysis of economic models and financial systems
- **Poetry** - Creative writing and reflections
- **Self-Improvement** - Personal development and growth
- **Tech Concepts** - Educational content on technology
- **Random Thoughts** - Miscellaneous articles

Recent additions include comprehensive guides on:
- Meta-Learning and Learning to Learn
- Federated Learning with industry applications
- Various AI research topics and implementations

## SEO Configuration

### Meta Tags

Automatically generated from `config.yaml` and individual page metadata. Open Graph tags are included for social media sharing.

### Sitemap

The `freeze.py` script generates `docs/sitemap.xml` automatically for search engine indexing.

## Troubleshooting

### Frozen-Flask doesn't find blog posts or projects

Ensure:
- Blog posts are in `blog/category/` directories with proper frontmatter
- Portfolio projects have `index.md` files in their folders
- File extensions are `.md`
- Frontmatter format is correct (YAML between `---` markers)

### Dark mode doesn't persist

Check that browser localStorage is enabled. The site defaults to dark mode on first visit.

### Custom domain not working

1. Verify `CNAME` file exists in `docs/` after running `freeze.py`
2. Check DNS settings at your registrar
3. Wait for DNS propagation (up to 48 hours)
4. Verify GitHub Pages settings show "DNS check successful"
5. Ensure "Enforce HTTPS" is enabled in GitHub Pages settings

### Images not loading

- Ensure images are in `static/img/` or project-specific folders
- Use correct paths in templates and markdown
- Check image paths are preserved after freezing

## Security

- No server-side code runs on GitHub Pages (static files only)
- No database or user authentication required
- All assets served over HTTPS
- Content Security Policy compatible

## License

Feel free to use this template for your own personal website! Attribution appreciated but not required.

## Contributing

This is a personal website, but if you find bugs or have suggestions, feel free to open an issue or submit a pull request.

## Contact

- **Website**: [omegamakena.co.ke](https://omegamakena.co.ke)
- **GitHub**: [@Omega-Makena](https://github.com/Omega-Makena)
- **LinkedIn**: [omega-makena](https://www.linkedin.com/in/omega-makena)
- **Email**: mwebiamakenaa@gmail.com
- **Alternative Email**: omegamakena@techtwirls.co.ke

---

**Built by Omega Makena**

*Last updated: November 2025*
