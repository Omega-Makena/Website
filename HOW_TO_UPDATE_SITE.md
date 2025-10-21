# How to Update Your Website - No Code Required! 🎉

This guide shows you how to update your entire website by **only editing configuration files** - no Python code needed!

---

## 🎨 Updating Personal Information

Edit the `config.yaml` file to update your personal information, site settings, and social links.

### Change Your Name & Tagline

```yaml
site:
  title: Your Name
  tagline: Your Professional Title
  description: Brief description of your site
```

### Update Your Bio

```yaml
personal:
  name: Your Name
  email: your@email.com
  location: Your Location
  bio: |
    <p>Your first paragraph here...</p>
    <p>Your second paragraph here...</p>
    <p>Your third paragraph here...</p>
```

### Update Social Links

```yaml
social:
  github: https://github.com/yourusername
  linkedin: https://linkedin.com/in/yourusername
  twitter: https://twitter.com/yourusername  # Optional
  email: your@email.com
```

### Change Blog Categories

```yaml
blog_categories:
  - Technology
  - Design
  - Productivity
  - Travel
  - Photography
```

---

## 📝 Adding Blog Posts

1. Create a new Markdown file in the `posts/` directory
2. Name it descriptively: `my-awesome-post.md`
3. Add frontmatter at the top:

```markdown
title: My Awesome Blog Post
date: 2025-01-20
category: Technology
author: Your Name
description: A brief description of your post

---

## Your Content Here

Write your blog post content in Markdown format...
```

### Supported Markdown Features

- **Headings**: `## Heading 2`, `### Heading 3`
- **Bold**: `**bold text**`
- **Italic**: `*italic text*`
- **Links**: `[link text](https://url.com)`
- **Images**: `![alt text](/static/img/image.jpg)`
- **Code blocks**: Use triple backticks with language
- **Lists**: Bullet points and numbered lists
- **Blockquotes**: `> Quote text`
- **Tables**: GitHub-style tables

---

## 🚀 Adding Projects

Create a new YAML file in the `projects/` directory:

### Quick Example

File: `projects/my-new-project.yaml`

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

**That's it!** Your project will automatically appear on the portfolio page.

> 📖 See `HOW_TO_ADD_PROJECTS.md` for detailed project documentation

---

## 🖼️ Adding Images

### Profile Photo
1. Add your photo to `static/img/profile.jpg`
2. Update `config.yaml` if using a different filename:
   ```yaml
   personal:
     profile_image: my-photo.png
   ```

### Project Images
1. Add images to `static/img/`
2. Reference them in project YAML files:
   ```yaml
   image: project-screenshot.jpg
   ```

### Blog Post Images
1. Add images to `static/img/`
2. Reference in Markdown:
   ```markdown
   ![Description](/static/img/blog-image.jpg)
   ```

---

## 🎨 Customizing Colors & Design

Colors are defined in `templates/base.html`. Look for the TailwindCSS config section:

```javascript
colors: {
    light: {
        bg: '#F9FAFB',      // Background color
        card: '#FFFFFF',     // Card color
        text: '#1C1C1C',    // Text color
        accent: '#1E3A8A',  // Accent color (buttons, links)
    },
    dark: {
        bg: '#0F172A',      // Dark mode background
        // ... etc
    }
}
```

Change the hex codes to your preferred colors!

---

## 🔄 Workflow: Making Updates

### Local Development

```bash
# 1. Edit files (config.yaml, project YAML, blog posts, etc.)

# 2. Test locally
python app.py
# Visit http://localhost:5000

# 3. If everything looks good, proceed to deployment
```

### Deployment to GitHub Pages

```bash
# 1. Generate static files
python freeze.py

# 2. Add and commit changes
git add .
git commit -m "Update website content"

# 3. Push to GitHub
git push origin main

# 4. Wait 2-3 minutes for GitHub Pages to update
```

---

## 📁 File Structure Reference

```
.
├── config.yaml              # ⭐ Main site configuration
├── projects/                # ⭐ Project YAML files
│   ├── project-1.yaml
│   ├── project-2.yaml
│   └── project-3.yaml
├── posts/                   # ⭐ Blog posts (Markdown)
│   ├── my-post-1.md
│   └── my-post-2.md
├── static/
│   └── img/                # ⭐ Images
│       ├── profile.jpg
│       └── project-images.jpg
├── templates/              # HTML templates (rarely need to edit)
│   ├── base.html
│   ├── index.html
│   ├── portfolio.html
│   ├── blog.html
│   └── post.html
├── app.py                  # Flask app (don't need to edit)
├── freeze.py              # Static site generator (don't need to edit)
└── docs/                  # Generated static site (auto-created)
```

**Files you'll edit regularly:**
- `config.yaml` - Site settings
- `projects/*.yaml` - Portfolio projects  
- `posts/*.md` - Blog posts
- `static/img/*` - Images

**Files you'll rarely/never edit:**
- `app.py` - Backend logic
- `freeze.py` - Build script
- `templates/*.html` - Page layouts

---

## ✅ Quick Checklist

### Before Publishing Content

- [ ] Spell-check all content
- [ ] Test all links (URLs should start with https://)
- [ ] Verify images load correctly
- [ ] Check mobile responsiveness (`F12` → Toggle device toolbar)
- [ ] Test dark mode toggle
- [ ] Run locally: `python app.py`
- [ ] Generate static files: `python freeze.py`

### After Pushing to GitHub

- [ ] Wait 2-3 minutes for build
- [ ] Visit your live site
- [ ] Test navigation
- [ ] Check new content appears
- [ ] Verify on mobile device

---

## 🐛 Troubleshooting

### Content Not Updating?

1. Check YAML syntax is correct (use spaces, not tabs)
2. Ensure file is saved
3. Run `python freeze.py` again
4. Clear browser cache (`Ctrl+F5`)

### Images Not Loading?

1. Verify image is in `static/img/`
2. Check filename matches exactly (case-sensitive)
3. Use `/static/img/filename.jpg` path format

### Blog Post Not Appearing?

1. Check frontmatter format is correct
2. Verify category exists in `config.yaml`
3. Ensure file extension is `.md`
4. Check date format is `YYYY-MM-DD`

### YAML Syntax Errors?

Common mistakes:
- Using tabs instead of spaces (use 2 spaces)
- Missing colons after keys
- Incorrect indentation
- Quotes around URLs (not needed)

---

## 💡 Tips & Best Practices

### Writing Great Project Descriptions
- Focus on impact and results
- Keep it concise (1-2 sentences)
- Mention specific achievements (e.g., "Reduced load time by 40%")

### Blog Post SEO
- Use descriptive titles
- Write compelling descriptions (shows in blog listing)
- Use headers (`##`, `###`) for structure
- Add alt text to images
- Include internal links to other posts

### Image Optimization
- Compress images before uploading (<500KB)
- Use modern formats (WebP, optimized JPG)
- Maintain consistent aspect ratios
- Add descriptive filenames

### Organizing Content
- Use meaningful project file names (`ai-chatbot.yaml`)
- Create dated blog posts (`2025-01-20-my-post.md`)
- Group related images in subdirectories if needed

---

## 🎓 Learning Resources

### YAML Syntax
- [YAML Tutorial](https://yaml.org/)
- [YAML Validator](https://www.yamllint.com/)

### Markdown
- [Markdown Guide](https://www.markdownguide.org/)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

### Git & GitHub
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)

---

## 📞 Need Help?

If you encounter issues:

1. Check file syntax carefully
2. Review error messages from `python app.py` or `python freeze.py`
3. Compare your files to the example files provided
4. Test in a fresh browser window (incognito mode)

---

**Happy updating! 🎉**

*Remember: You control your entire website by editing simple configuration files - no coding required!*

