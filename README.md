# Personal Website Template

A professional personal website template built with Flask, Jinja2, and TailwindCSS. Features a portfolio, multi-category blog, dark mode, and static site generation for deployment to GitHub Pages.

## Features

- Clean, modern design with dark mode support (defaults to dark)
- Responsive mobile-first layout
- Markdown-based blog with category organization
- Folder-based portfolio structure for projects
- Zero-code content management (just add markdown files)
- Static site generation for free GitHub Pages hosting

## Prerequisites

Before you start, make sure you have:
- Python 3.8 or higher installed
- Git installed
- A GitHub account

## Step-by-Step Setup Guide

### Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/Omega-Makena/Website.git
cd Website
```

This creates a local copy of the template on your computer.

### Step 2: Create a Virtual Environment

A virtual environment keeps your project dependencies separate from other Python projects:

```bash
python -m venv venv
```

This creates a new folder called `venv` in your project directory.

### Step 3: Activate the Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal prompt, indicating the virtual environment is active.

### Step 4: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

Wait for the installation to complete. You should see a list of packages being installed.

### Step 5: Configure Your Site

Open `config.yaml` in a text editor and replace the placeholder information with your own:

```yaml
site:
  title: Your Name
  tagline: Your Professional Title
  description: A brief description of who you are
  url: https://yourusername.github.io/website

personal:
  name: Your Name
  email: your@email.com
  location: Your Location
  bio: |
    <p>Write a paragraph about yourself here.</p>
    <p>Add more paragraphs as needed.</p>

social:
  github: https://github.com/yourusername
  linkedin: https://linkedin.com/in/yourusername
  email: your@email.com
```

Save the file after making your changes.

### Step 6: Add Your Profile Image

1. Find or create a professional photo of yourself
2. Name it `profile.jpg`
3. Place it in the `static/img/` folder

Your photo should be square (e.g., 400x400 pixels) for best results.

### Step 7: Test Your Site Locally

Start the development server:

```bash
python app.py
```

You should see output like:
```
* Running on http://127.0.0.1:5000
```

Open your web browser and visit `http://localhost:5000` to see your site.

The site auto-reloads when you make changes to files, so you can keep the browser open and refresh to see updates.

### Step 8: Add Your First Blog Post

Create a new markdown file in one of the category folders under `blog/`. For example:

**File:** `blog/ai-ml/my-first-post.md`

```markdown
---
title: My First Blog Post
date: 2025-01-15
category: ai-ml
author: Your Name
description: This is what my first post is about
---

# My First Blog Post

This is the content of my first blog post. Write in Markdown here.

## Subheading

More content here...

- Bullet point 1
- Bullet point 2

**Bold text** and *italic text* also work.
```

Save the file and refresh your browser to see the new post.

**Available blog categories:**
- `ai-ml` - AI & Machine Learning
- `finance-economics` - Finance & Economics
- `poetry` - Poetry
- `self-improvement` - Self-Improvement
- `tech-concepts` - Tech Concepts
- `random` - Random Thoughts

### Step 9: Add a Portfolio Project

Create a new folder for your project under `portfolio/projects/`:

1. Create folder: `portfolio/projects/my-project/`
2. Create file: `portfolio/projects/my-project/index.md`

**File content:**
```markdown
---
title: My First Project
description: A brief description of what this project does
tech:
  - Python
  - JavaScript
  - React
live_url: https://myproject.com
github_url: https://github.com/yourusername/project
image: screenshot.jpg
order: 1
featured: true
---

# Project Details

Write a detailed description of your project here.

## Features

- Feature 1
- Feature 2
- Feature 3

Include screenshots, code examples, or anything else that showcases your work.
```

Save the file and refresh your browser. The project will appear on your portfolio page.

### Step 10: Generate the Static Site

When you're ready to deploy, stop the development server (press `Ctrl+C` in the terminal) and generate static HTML files:

```bash
python freeze.py
```

This creates a `docs/` folder containing all the HTML files for your website.

You can test the static site locally:
```bash
cd docs
python -m http.server 8000
```

Visit `http://localhost:8000` to see the static version.

### Step 11: Deploy to GitHub Pages

1. **Push to GitHub:**
```bash
cd ..
git add .
git commit -m "My personal website"
git push origin main
```

2. **Configure GitHub Pages:**
   - Go to your repository on GitHub
   - Click on **Settings**
   - Scroll down to **Pages** section
   - Under **Source**, select:
     - Branch: `main`
     - Folder: `/docs`
   - Click **Save**

3. **Wait for deployment:**
   - GitHub will show "Your site is live at https://yourusername.github.io/website"
   - It may take a few minutes to become accessible

Your website is now live!

### Step 12: Set Up Custom Domain (Optional)

If you have your own domain name:

1. **Create CNAME file:**
```bash
echo "yourdomain.com" > CNAME
```

2. **Configure DNS:**
   At your domain registrar, add these A records:
   ```
   @ → 185.199.108.153
   @ → 185.199.109.153
   @ → 185.199.110.153
   @ → 185.199.111.153
   ```

3. **Push the CNAME file:**
```bash
python freeze.py  # This copies CNAME to docs/
git add docs/CNAME
git commit -m "Add custom domain"
git push origin main
```

4. **Enable HTTPS:**
   In GitHub Pages settings, check "Enforce HTTPS" once DNS has propagated (usually 24-48 hours)

### Step 13: Enable Analytics (Optional)

To track visits to your website:

1.  Go to [Google Analytics](https://analytics.google.com/) and create a free account.
2.  Create a new property for your website.
3.  Get your **Measurement ID** (it starts with `G-XX...`).
4.  Open `config.yaml` and paste it:
    ```yaml
    site:
      # ...
      google_analytics_id: "G-XXXXXXXXXX"
    ```
5.  Deploy your site using `python freeze.py` and git push.


## Project Structure Explained

```
.
├── app.py              # Main Flask application
├── arcs.py           # Static site generator
├── config.yaml        # Your site configuration
├── CNAME             # Custom domain (if applicable)
├── templates/        # HTML templates
│   ├── base.html    # Base layout with nav/footer
│   ├── index.html   # Home page
│   ├── portfolio.html    # Portfolio listing page
│   ├── project.html      # Individual project page
│   ├── blog.html         # Blog categories page
│   └── blog_category.html # Individual category page
├── blog/            # Your blog posts
│   └── [category]/  # Organized by category
├── portfolio/       # Your portfolio projects
│   └── projects/    # Each project in its own folder
├── static/          # Static files
│   └── img/        # Images (profile.jpg, etc.)
└── docs/           # Generated static site (deployed to GitHub Pages)
```

## Making Future Updates

Whenever you want to update your website:

1. **Add/edit content:**
   - Edit `config.yaml` for personal info
   - Add blog posts in `blog/category/`
   - Add projects in `portfolio/projects/`

2. **Test locally:**
```bash
python app.py
# Preview at http://localhost:5000
```

3. **Deploy changes:**
```bash
python freeze.py
git add .
git commit -m "Update website"
git push origin main
```

## Technologies Used

- **Flask** - Python web framework
- **Flask-FlatPages** - Markdown blog posts
- **Frozen-Flask** - Static site generation
- **TailwindCSS** - Styling framework
- **Jinja2** - Template engine

## Troubleshooting

**Virtual environment not activating:**
- Make sure you're in the correct directory
- Try using the full path: `python -m venv venv`

**Import errors when running app.py:**
- Make sure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

**Site not updating on GitHub Pages:**
- Make sure you ran `python freeze.py` before pushing
- Check that `/docs` folder is in the GitHub repository
- Wait a few minutes for GitHub to rebuild

**Images not showing:**
- Make sure images are in `static/img/` or the project folder
- Use proper file paths in markdown files

## Support

For issues or questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Read the code comments for implementation details

## License

Free to use for personal websites only. Commercial use is not permitted. Attribution appreciated but not required.

---

Good luck building your personal website!
