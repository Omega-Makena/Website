from flask import Flask, render_template, abort
from flask_flatpages import FlatPages
from datetime import datetime
import os
import yaml
from pathlib import Path

app = Flask(__name__)

# Configuration
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'blog'
app.config['FLATPAGES_MARKDOWN_EXTENSIONS'] = ['codehilite', 'fenced_code', 'tables']

flatpages = FlatPages(app)

# Load site configuration
def load_config():
    """Load site configuration from config.yaml"""
    config_path = Path('config.yaml')
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return {}

# Load projects from portfolio/projects directory
def load_projects():
    """Load all projects from the portfolio/projects directory"""
    projects = []
    projects_dir = Path('portfolio/projects')
    
    if projects_dir.exists():
        for project_folder in projects_dir.iterdir():
            if project_folder.is_dir():
                index_file = project_folder / 'index.md'
                if index_file.exists():
                    try:
                        with open(index_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            # Parse frontmatter
                            if content.startswith('---'):
                                parts = content.split('---', 2)
                                if len(parts) >= 3:
                                    frontmatter = yaml.safe_load(parts[1])
                                    # Store markdown content without frontmatter
                                    frontmatter['content'] = parts[2].strip()
                                    frontmatter['slug'] = project_folder.name
                                    projects.append(frontmatter)
                    except Exception as e:
                        print(f"Error loading project {index_file}: {e}")
    
    # Sort by order field (if exists), then by title
    projects.sort(key=lambda x: (x.get('order', 999), x.get('title', '')))
    return projects

# Load configuration and projects
SITE_CONFIG = load_config()
BLOG_CATEGORIES = SITE_CONFIG.get('blog_categories', [])
PROJECTS = load_projects()

@app.route('/')
def index():
    """Home / About page"""
    return render_template('index.html')

@app.route('/portfolio/')
def portfolio():
    """Portfolio page with projects"""
    return render_template('portfolio.html', projects=PROJECTS)

@app.route('/portfolio/<path:project_slug>/')
def project_detail(project_slug):
    """Individual project detail page"""
    # Find the project by slug
    project = None
    for p in PROJECTS:
        if p.get('slug') == project_slug:
            project = p
            break
    
    if not project:
        abort(404)
    
    return render_template('project.html', project=project)

@app.route('/blog/')
def blog():
    """Blog categories page"""
    # Get all posts and group by their directory (category)
    posts_by_category = {}
    all_posts = list(flatpages)
    
    # Group by subdirectory path
    for post in all_posts:
        # Get the category from the path (e.g., 'ai-ml/learning-federated-learning.md' -> 'ai-ml')
        path_parts = post.path.split('/')
        if len(path_parts) > 1:
            category_folder = path_parts[0]
        else:
            category_folder = 'general'
        
        if category_folder not in posts_by_category:
            posts_by_category[category_folder] = []
        posts_by_category[category_folder].append(post)
    
    # Sort posts by date within each category
    for category in posts_by_category:
        posts_by_category[category].sort(
            key=lambda x: x.meta.get('date', datetime.min),
            reverse=True
        )
    
    return render_template('blog.html', 
                         categories=sorted(posts_by_category.keys()),
                         posts_by_category=posts_by_category)

@app.route('/blog/<path:path>')
def blog_post(path):
    """Individual blog post"""
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

@app.template_filter('format_date')
def format_date(date):
    """Format date for display"""
    if isinstance(date, str):
        date = datetime.strptime(date, '%Y-%m-%d')
    return date.strftime('%B %d, %Y')

@app.context_processor
def inject_globals():
    """Inject global variables into all templates"""
    return {
        'current_year': datetime.now().year,
        'config': SITE_CONFIG
    }

if __name__ == '__main__':
    app.run(debug=True, port=5000)


