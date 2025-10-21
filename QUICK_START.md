# 🚀 Quick Start Guide

Get your dynamic website up and running in 5 minutes!

---

## Step 1: Setup (One Time Only)

```bash
# Clone the repository
git clone https://github.com/Omega-Makena/Website.git
cd Website

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Step 2: Customize Your Site

### Edit `config.yaml`:

```yaml
site:
  title: Your Name
  tagline: Your Professional Title

personal:
  name: Your Name
  email: your@email.com
  bio: |
    <p>Your bio paragraph 1</p>
    <p>Your bio paragraph 2</p>

social:
  github: https://github.com/yourusername
  linkedin: https://linkedin.com/in/yourusername
  email: your@email.com
```

### Add Your Projects

Create `projects/my-first-project.yaml`:

```yaml
title: My Awesome Project
description: What it does and why it's cool
tech:
  - Python
  - React
  - Docker
live_url: https://myproject.com
github_url: https://github.com/yourusername/project
order: 1
featured: true
```

### Add Blog Posts

Create `posts/my-first-post.md`:

```markdown
title: My First Blog Post
date: 2025-01-20
category: Technology
author: Your Name
description: A brief description

---

## Welcome!

Your blog post content here...
```

---

## Step 3: Test Locally

```bash
python app.py
```

Visit `http://localhost:5000` to see your site!

---

## Step 4: Deploy to GitHub Pages

```bash
# Generate static files
python freeze.py

# Commit and push
git add .
git commit -m "Update website"
git push origin main
```

Wait 2-3 minutes and your site will be live!

---

## 📁 What Files Do I Edit?

**✅ Edit These Regularly:**
- `config.yaml` - Your personal information
- `projects/*.yaml` - Your portfolio projects
- `posts/*.md` - Your blog posts
- `static/img/*` - Your images

**❌ Don't Edit These:**
- `app.py` - Backend (handles everything automatically)
- `templates/*.html` - Page layouts
- `freeze.py` - Build script

---

## 🔄 Daily Workflow

1. Make changes (edit YAML/Markdown files)
2. Test: `python app.py`
3. Build: `python freeze.py`
4. Deploy: `git add . && git commit -m "Update" && git push`

---

## 📚 Full Documentation

- **[HOW_TO_UPDATE_SITE.md](HOW_TO_UPDATE_SITE.md)** - Complete guide
- **[HOW_TO_ADD_PROJECTS.md](HOW_TO_ADD_PROJECTS.md)** - Project details
- **[EXAMPLE_PROJECT.yaml](EXAMPLE_PROJECT.yaml)** - Template file

---

**That's it! You now have a fully dynamic website with no code editing required! 🎉**

