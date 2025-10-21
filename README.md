# Omega Makena - Personal Website

A professional personal website built with **Flask + Jinja2** and **TailwindCSS**, featuring a portfolio, multi-category blog, and dark mode toggle. Designed for deployment to **GitHub Pages**.

## ✨ **NEW: Fully Dynamic Content Management - NO CODE REQUIRED!**

**Zero code editing needed!** Everything is managed with simple files:
- 📝 **Add Blog Posts** → Drop `.md` files in `posts/` folder
- 🚀 **Add Projects** → Drop `.yaml` files in `projects/` folder
- 🎨 **Update Personal Info** → Edit `config.yaml` file
- 🖼️ **Add Images** → Drop files in `static/img/` folder

**That's it!** Run `python freeze.py` and `git push` to deploy.

> 📖 **Quick Start Guides:**
> - [HOW_TO_ADD_BLOG_POSTS.md](HOW_TO_ADD_BLOG_POSTS.md) - Write blog posts (Markdown files)
> - [HOW_TO_ADD_PROJECTS.md](HOW_TO_ADD_PROJECTS.md) - Add portfolio projects (YAML files)
> - [HOW_TO_UPDATE_SITE.md](HOW_TO_UPDATE_SITE.md) - Complete site management guide
> - [GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md) - Deployment instructions

![Website Preview](https://img.shields.io/badge/Status-Production-brightgreen)

## 🌟 Features

- **Modern Design**: Clean, academic-modern aesthetic with custom color palette
- **Dark Mode**: Seamless light/dark theme toggle with localStorage persistence
- **Responsive**: Mobile-first design that works on all devices
- **Blog System**: Markdown-based blog with 7 categories
- **Portfolio**: Showcase projects with live demos and GitHub links
- **SEO Optimized**: Meta tags, Open Graph, and social card support
- **Static Site Generation**: Converts Flask app to static HTML for GitHub Pages

## 📁 Project Structure

```
.
├── app.py                  # Flask application
├── freeze.py              # Static site generator
├── requirements.txt       # Python dependencies
├── CNAME                  # Custom domain configuration
├── templates/             # Jinja2 templates
│   ├── base.html         # Base template with navbar/footer
│   ├── index.html        # Home/About page
│   ├── portfolio.html    # Portfolio page
│   ├── blog.html         # Blog categories page
│   └── post.html         # Individual blog post
├── posts/                 # Markdown blog posts
│   ├── poetry-digital-age.md
│   ├── ai-transformer-revolution.md
│   ├── ai-trends-2025.md
│   ├── psychology-flow-state.md
│   ├── self-improvement-learning.md
│   ├── paper-review-alphafold.md
│   └── my-paper-ai-equity.md
├── static/               # Static assets
│   └── img/             # Images (profile, favicon, etc.)
└── docs/                # Generated static site (created by freeze.py)
```

## 🚀 Quick Start

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

Edit `config.yaml` to update your personal information:

```yaml
site:
  title: Your Name
  tagline: Your Professional Title

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

### 4. Run Development Server

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## 🎨 Customization (No Code Required!)

### Update Personal Information

Edit `config.yaml`:

```yaml
site:
  title: Your Name
  tagline: Your Title
  description: Your site description

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

Create a new YAML file in `projects/`:

**File:** `projects/my-project.yaml`

```yaml
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
```

That's it! No code editing required. See [HOW_TO_ADD_PROJECTS.md](HOW_TO_ADD_PROJECTS.md) for details.

### Add Blog Posts

Create markdown files in the `posts/` directory with this frontmatter:

```markdown
title: Your Post Title
date: 2025-01-15
category: AI
author: Omega Makena
description: A brief description of your post

---

## Your Content Here

Write your blog post content in Markdown...
```

**Available Categories**:
- Poetry
- AI
- Trends
- Psychology
- Self-Improvement
- Paper Review
- My Papers

### Customize Colors

The color palette is defined in `templates/base.html` (TailwindCSS config):

```javascript
colors: {
    light: {
        bg: '#F9FAFB',
        card: '#FFFFFF',
        text: '#1C1C1C',
        // ... etc
    },
    dark: {
        bg: '#0F172A',
        // ... etc
    }
}
```

### Add Images

Place images in `static/img/`:
- `profile.jpg` - Your professional photo
- `favicon.ico` - Browser favicon
- `apple-touch-icon.png` - iOS home screen icon
- `social-card.jpg` - Open Graph preview image (1200x630px)

## 📦 Deployment to GitHub Pages

### Step 1: Generate Static Site

```bash
python freeze.py
```

This creates a `docs/` folder with static HTML files.

### Step 2: Configure GitHub Repository

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select:
   - Branch: `main`
   - Folder: `/docs`
4. Click **Save**

### Step 3: Configure Custom Domain (Optional)

The `CNAME` file is already configured with `omegamakena.co.ke`.

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
git commit -m "Deploy website"
git push origin main
```

### Step 5: Enable HTTPS

In GitHub Pages settings, check **Enforce HTTPS** (available after DNS propagates).

## 🔧 Development Workflow

### Local Development

```bash
# Run Flask dev server
python app.py

# Make changes to templates/posts
# Refresh browser to see changes
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

## 📝 Blog Writing Tips

### Markdown Support

The blog supports standard Markdown plus:

- **Code blocks** with syntax highlighting
- **Tables**
- **Blockquotes**
- **Lists** (ordered and unordered)
- **Links** and **images**
- **Headings** (H2, H3 recommended)

### SEO Best Practices

- Use descriptive titles
- Write compelling descriptions (shows in blog listing)
- Include relevant keywords naturally
- Use proper heading hierarchy (H2 → H3 → H4)
- Add alt text to images

## 🎯 SEO Configuration

### Meta Tags

Update in `templates/base.html`:
- `og:image` - Social share preview image URL
- `og:description` - Default site description
- Twitter card metadata

### Sitemap (Optional)

Add to `freeze.py` to generate `sitemap.xml` for search engines.

## 🐛 Troubleshooting

### Frozen-Flask doesn't find blog posts

Ensure:
- Posts are in `posts/` directory
- Frontmatter format is correct
- File extension is `.md`

### Dark mode doesn't persist

Check browser localStorage is enabled.

### Custom domain not working

1. Verify CNAME file exists in `docs/` after running `freeze.py`
2. Check DNS settings at your registrar
3. Wait for DNS propagation (up to 48 hours)
4. Verify GitHub Pages settings show "DNS check successful"

### Images not loading

- Ensure images are in `static/img/`
- Use `/static/img/filename.jpg` in templates
- Check image paths are correct after freezing

## 📚 Technologies Used

- **Flask** - Web framework
- **Flask-FlatPages** - Markdown blog posts
- **Frozen-Flask** - Static site generation
- **TailwindCSS** - Styling (CDN version)
- **Jinja2** - Templating
- **Markdown** - Blog content format

## 🔐 Security

- No server-side code runs on GitHub Pages (static files only)
- No database or user authentication
- All assets served over HTTPS
- Content Security Policy compatible

## 📄 License

Feel free to use this template for your own personal website! Attribution appreciated but not required.

## 🤝 Contributing

This is a personal website, but if you find bugs or have suggestions, feel free to open an issue!

## 📧 Contact

- **Website**: [omegamakena.co.ke](https://omegamakena.co.ke)
- **GitHub**: [@Omega-Makena](https://github.com/Omega-Makena)
- **LinkedIn**: [omega-makena](https://linkedin.com/in/omega-makena)
- **Email**: omega@omegamakena.co.ke

---

**Built with ❤️ by Omega Makena**

*Last updated: January 2025*
