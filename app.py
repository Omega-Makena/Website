from flask import Flask, render_template, abort, redirect, url_for
from flask_flatpages import FlatPages
from datetime import datetime
import yaml
from pathlib import Path
import os

app = Flask(__name__)

# Configuration
app.config['FLATPAGES_AUTO_RELOAD'] = True
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = '.'  # Scan the entire project
app.config['FLATPAGES_MARKDOWN_EXTENSIONS'] = ['codehilite', 'fenced_code', 'tables']
# Exclude vendor folders to avoid parsing unnecessary files
app.config['FLATPAGES_EXCLUDE'] = ['venv', 'node_modules']


flatpages = FlatPages(app)

# Load site configuration
def load_config():
    """Load site configuration from config.yaml"""
    config_path = Path('config.yaml')
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return {}

# Load configuration
SITE_CONFIG = load_config()

@app.route('/')
def index():
    """Home / About page"""
    return render_template('index.html')

def render_flatpage(path):
    """Render a FlatPages entry or 404"""
    page = flatpages.get(path)
    if not page:
        abort(404)
    return render_template('page.html', page=page)

@app.route('/about/')
def about():
    """About page"""
    return render_flatpage('about')

@app.route('/work-with-me/')
def work_with_me():
    """Collaboration page"""
    return render_flatpage('work-with-me')

@app.route('/scarcity/')
def scarcity_overview():
    """Default Scarcity overview"""
    return render_flatpage('scarcity/overview')

@app.route('/scarcity/<path:subpath>')
def scarcity_page(subpath):
    """Scarcity subpages"""
    return render_flatpage(f'scarcity/{subpath}')

@app.route('/library/')
def library_index():
    """Library landing showing grouped teaching notes"""
    pages = [p for p in flatpages if p.path.startswith('library/')]
    grouped = {}
    for p in pages:
        parts = p.path.split('/')
        category = parts[1] if len(parts) > 1 else 'general'
        grouped.setdefault(category, []).append(p)
    for items in grouped.values():
        items.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)
    ordered = [(k, grouped[k]) for k in sorted(grouped.keys())]
    return render_template('library_index.html', grouped=ordered)

@app.route('/library/<path:subpath>')
def library_page(subpath):
    """Library subpages"""
    return render_flatpage(f'library/{subpath}')

@app.route('/research-log/')
def research_log_index():
    """Research log index"""
    logs = [p for p in flatpages if p.path.startswith('research-log/')]
    logs.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)
    return render_template('research_log.html', logs=logs)

@app.route('/research-log/<path:subpath>')
def research_log_page(subpath):
    """Research log entry"""
    return render_flatpage(f'research-log/{subpath}')

@app.route('/writing/')
def writing_index():
    """Writing landing grouped by subsection"""
    pages = [p for p in flatpages if p.path.startswith('writing/')]
    grouped = {}
    for p in pages:
        parts = p.path.split('/')
        subsection = p.meta.get('subsection') or (parts[1] if len(parts) > 1 else 'notes')
        grouped.setdefault(subsection, []).append(p)
    for items in grouped.values():
        items.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)
    ordered = [(k, grouped[k]) for k in sorted(grouped.keys())]
    return render_template('writing_index.html', grouped=ordered)

@app.route('/writing/<path:subpath>')
def writing_page(subpath):
    """Writing subpages"""
    return render_flatpage(f'writing/{subpath}')

@app.route('/portfolio/')
def portfolio():
    """Portfolio page with projects"""
    # Filter for pages that are inside the portfolio/projects directory
    projects = [p for p in flatpages if p.path.startswith('portfolio/projects/')]
    
    # Extract the slug from the path (e.g., 'portfolio/projects/my-project/index' -> 'my-project')
    for p in projects:
        p.meta['slug'] = p.path.split('/')[-2]

    # Sort by order field (if exists), then by title
    projects.sort(key=lambda x: (x.meta.get('order', 999), x.meta.get('title', '')))
    
    return render_template('portfolio.html', projects=projects)

@app.route('/portfolio/<path:project_slug>/')
def project_detail(project_slug):
    """Individual project detail page"""
    # Construct the full path for the flatpage
    path = f'portfolio/projects/{project_slug}/index'
    project = flatpages.get(path)
    
    if not project:
        abort(404)
        
    project.meta['slug'] = project_slug
    
    return render_template('project.html', project=project)

@app.route('/blog/')
def blog():
    """Blog categories page"""
    # Get all posts that are inside the blog directory
    all_posts = [p for p in flatpages if p.path.startswith('blog/')]
    
    posts_by_category = {}
    
    for post in all_posts:
        # Path is now like 'blog/ai-ml/post-name'
        path_parts = post.path.split('/')
        
        # Ensure it's a blog post and not a project file that might have been moved
        if len(path_parts) > 2 and path_parts[0] == 'blog':
            category_folder = path_parts[1]
            
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

@app.route('/blog/<category>/')
def blog_category(category):
    """Blog posts by category"""
    # Path is now f'blog/{category}/'
    category_path_prefix = f'blog/{category}/'
    category_posts = [p for p in flatpages if p.path.startswith(category_path_prefix)]
    
    # Sort by date (newest first)
    category_posts.sort(
        key=lambda x: x.meta.get('date', datetime.min),
        reverse=True
    )
    
    # Category display name from config or generate it
    category_names = SITE_CONFIG.get('blog_category_names', {})
    category_name = category_names.get(category, category.replace('-', ' ').title())
    
    return render_template('blog_category.html', 
                         category=category,
                         category_name=category_name,
                         posts=category_posts)

@app.route('/blog/<path:path>')
def blog_post(path):
    """Individual blog post"""
    # The full path from the FLATPAGES_ROOT is needed
    full_path = f'blog/{path}'
    post = flatpages.get(full_path)
    if not post:
        abort(404)
    return render_template('post.html', post=post)

@app.template_filter('format_date')
def format_date(date):
    """Format date for display"""
    if isinstance(date, str):
        try:
            # Handle 'YYYY-MM-DD'
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            # Handle other formats if necessary, or return as is
            return date
    if isinstance(date, datetime):
        return date.strftime('%B %d, %Y')
    return date

@app.context_processor
def inject_globals():
    """Inject global variables into all templates"""
    return {
        'current_year': datetime.now().year,
        'config': SITE_CONFIG
    }

if __name__ == '__main__':
    # Use a different port to avoid conflicts with common services
    app.run(debug=True, port=5001)

