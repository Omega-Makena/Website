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
app.config['FLATPAGES_ROOT'] = 'posts'
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

# Load projects from YAML files
def load_projects():
    """Load all projects from the projects directory"""
    projects = []
    projects_dir = Path('projects')
    
    if projects_dir.exists():
        for yaml_file in projects_dir.glob('*.yaml'):
            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    project = yaml.safe_load(f)
                    if project:
                        projects.append(project)
            except Exception as e:
                print(f"Error loading project {yaml_file}: {e}")
    
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

@app.route('/blog/')
def blog():
    """Blog categories page"""
    # Group posts by category
    posts_by_category = {}
    for category in BLOG_CATEGORIES:
        posts_by_category[category] = [
            post for post in flatpages 
            if post.meta.get('category') == category
        ]
        # Sort by date (newest first)
        posts_by_category[category].sort(
            key=lambda x: x.meta.get('date', datetime.min),
            reverse=True
        )
    
    return render_template('blog.html', 
                         categories=BLOG_CATEGORIES,
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


