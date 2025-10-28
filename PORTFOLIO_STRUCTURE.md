# New Portfolio Structure

The portfolio has been reorganized to use a folder-based structure instead of individual YAML files.

## Directory Structure

```
/portfolio
└── /projects
    ├── /online-learning/
    │   ├── index.md
    │   └── screenshots/
    │       └── results.png
    │
    ├── /scarcity/
    │   ├── index.md
    │   ├── architecture-diagram.png
    │   ├── simulation-demo.gif
    │   ├── paper.pdf
    │   └── repo-link.txt
    │
    ├── /sarima/
    │   ├── index.md
    │   ├── chart.png
    │   └── model-evaluation.png
    │
    ├── /anomaly-detection/
    │   ├── index.md
    │   ├── roc-curve.png
    │   └── detection-demo.gif
    │
    └── /quant-model/
        ├── index.md
        ├── risk-forecast.png
        ├── correlation-heatmap.png
        └── results.pdf
```

## How to Add a New Project

1. Create a new folder under `portfolio/projects/` with a URL-friendly name (use hyphens, no spaces)

2. Create an `index.md` file in that folder with the following structure:

```markdown
---
title: Project Title
description: A brief description of your project
tech:
  - Python
  - TensorFlow
  - React
live_url: https://your-project.com
github_url: https://github.com/username/project
order: 1
featured: true
image: screenshot.png
paper: paper.pdf  # Optional
---

## Project Content

Write your project details here in Markdown...

### Features

- Feature 1
- Feature 2

## Results

Your results and outcomes here...
```

3. Add any assets (images, PDFs, etc.) to the project folder

4. Reference the assets in your `index.md` using `image: filename.png` in the frontmatter

## Frontmatter Fields

- **title** (required): Project name
- **description** (required): Brief description
- **tech** (required): List of technologies used
- **live_url** (optional): Link to live demo
- **github_url** (optional): Link to GitHub repo
- **order** (optional): Display order (lower = first)
- **featured** (optional): Set to `true` to highlight
- **image** (optional): Filename of main image in this folder
- **paper** (optional): PDF filename if available

## Routes

- **Portfolio List**: `/portfolio/` - Shows all projects
- **Project Detail**: `/portfolio/{project-slug}/` - Shows individual project

The slug is automatically generated from the folder name.

## Benefits of This Structure

1. ✅ All project assets are co-located with the project
2. ✅ Easy to add images, PDFs, GIFs, etc.
3. ✅ Markdown content is more flexible than YAML
4. ✅ Better organization for multiple assets per project
5. ✅ Easy to version control and share projects

