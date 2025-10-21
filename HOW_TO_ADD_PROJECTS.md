# How to Add Projects to Your Website

This guide explains how to add new projects to your portfolio **without touching the Python code**.

## 📝 Adding a New Project

### Step 1: Create a YAML File

1. Navigate to the `projects/` directory
2. Create a new file named `your-project-name.yaml`
3. Use the template below:

```yaml
title: Your Project Title
description: A clear, compelling description of your project (1-2 sentences)
tech:
  - Python
  - React
  - Docker
  - PostgreSQL
live_url: https://your-project-demo.com
github_url: https://github.com/yourusername/your-repo
image: your-project-image.jpg
order: 3
featured: true
```

### Step 2: Add Project Image (Optional)

1. Place your project image in `static/img/`
2. Use the filename you specified in the `image` field
3. Recommended size: 800x600px or 16:9 aspect ratio

### Step 3: Deploy

That's it! Your project will automatically appear on your portfolio page.

For local testing:
```bash
python app.py
```

For deployment:
```bash
python freeze.py
git add .
git commit -m "Add new project"
git push
```

---

## 📋 Field Reference

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| `title` | ✅ Yes | Project name | `"AI Chat Bot"` |
| `description` | ✅ Yes | Brief project description | `"A conversational AI..."` |
| `tech` | ✅ Yes | List of technologies used | `["Python", "Flask"]` |
| `live_url` | ❌ No | Link to live demo or main URL | `"https://myproject.com"` |
| `github_url` | ❌ No | GitHub repository URL | `"https://github.com/..."` |
| `image` | ❌ No | Image filename in `static/img/` | `"project.jpg"` |
| `order` | ❌ No | Display order (lower = first) | `1` |
| `featured` | ❌ No | Highlight as featured project | `true` or `false` |

---

## 💡 Tips

### Project Order
- Projects are sorted by the `order` field (lowest first)
- If no `order` is specified, projects are sorted alphabetically by title
- Use gaps (1, 10, 20, 30) to easily insert projects later

### Technology Stack
- List technologies in order of importance
- Keep it to 4-6 items for visual appeal
- Use common, recognizable names (e.g., "React" not "React.js")

### Descriptions
- Keep it concise (1-2 sentences, ~150 characters)
- Focus on impact and results
- Avoid technical jargon unless necessary

### Images
- Use high-quality images (800x600px minimum)
- Maintain consistent aspect ratio (16:9 recommended)
- Optimize file size (<500KB)
- PNG or JPG format

---

## 🎯 Example Projects

### Web Application
```yaml
title: Task Manager Pro
description: A collaborative task management app with real-time updates and team analytics built for remote teams.
tech:
  - React
  - Node.js
  - MongoDB
  - Socket.io
live_url: https://taskmanagerpro.example.com
github_url: https://github.com/yourusername/task-manager
image: task-manager.jpg
order: 1
featured: true
```

### Machine Learning Project
```yaml
title: Sentiment Analyzer
description: NLP model achieving 94% accuracy in analyzing customer reviews across multiple languages.
tech:
  - Python
  - TensorFlow
  - BERT
  - FastAPI
github_url: https://github.com/yourusername/sentiment-analyzer
image: sentiment-analyzer.jpg
order: 2
featured: true
```

### Research Paper/Tool
```yaml
title: AlgoViz - Algorithm Visualizer
description: Interactive educational tool helping students understand sorting and pathfinding algorithms through visualization.
tech:
  - JavaScript
  - D3.js
  - HTML5
live_url: https://algoviz.example.com
github_url: https://github.com/yourusername/algoviz
image: algoviz.jpg
order: 3
featured: false
```

---

## ⚠️ Common Mistakes

1. **Incorrect YAML syntax**
   - Use spaces, not tabs for indentation
   - Use 2 spaces for nested items
   - Keep array items aligned

2. **Missing image files**
   - Make sure image exists in `static/img/`
   - Check filename matches exactly (case-sensitive)

3. **Invalid URLs**
   - Include `https://` prefix
   - Test links before deploying

4. **Too many technologies**
   - Limit to 4-6 key technologies
   - Focus on primary stack

---

## 🔄 Updating Existing Projects

1. Open the project's YAML file in `projects/`
2. Edit any field
3. Save the file
4. Redeploy: `python freeze.py` and push to GitHub

---

## 🗑️ Removing Projects

Simply delete the project's YAML file from the `projects/` directory and redeploy.

---

## ✅ Checklist

Before committing a new project:

- [ ] YAML file created in `projects/` directory
- [ ] All required fields filled (`title`, `description`, `tech`)
- [ ] Image added to `static/img/` (if using one)
- [ ] URLs tested and working
- [ ] Tested locally with `python app.py`
- [ ] Generated static files with `python freeze.py`
- [ ] Ready to commit and push

---

Need help? Check the existing project files in the `projects/` directory for examples!

