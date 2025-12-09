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
    research_logs = [
        p for p in flatpages
        if p.path.startswith('research-log/')
    ]
    research_logs.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)
    research_logs = research_logs[:3]

    library_highlights = [
        p for p in flatpages
        if p.path.startswith('library/')
    ]
    library_highlights.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)
    library_highlights = library_highlights[:3]

    writing_highlights = [
        p for p in flatpages
        if p.path.startswith('writing/')
    ]
    writing_highlights.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)
    writing_highlights = writing_highlights[:3]

    return render_template(
        'index.html',
        research_logs=research_logs,
        library_highlights=library_highlights,
        writing_highlights=writing_highlights,
    )

def render_flatpage(path):
    """Render a FlatPages entry or 404"""
    page = flatpages.get(path)
    if not page:
        abort(404)
    return render_template('page.html', page=page)

@app.route('/about')
@app.route('/about/')
def about():
    """About page"""
    return render_flatpage('about')

@app.route('/work-with-me')
@app.route('/work-with-me/')
def work_with_me():
    """Collaboration page"""
    return render_flatpage('work-with-me')

@app.route('/work/')
def work():
    """Work page"""
    page = flatpages.get('work')
    if not page:
        abort(404)
    return render_template('work.html', page=page)

@app.route('/scarcity')
@app.route('/scarcity/')
def scarcity_hub():
    """Scarcity hub page"""
    sections = [
        ('Overview', 'scarcity/overview'),
        ('Architecture', 'scarcity/architecture'),
        ('Components', 'scarcity/components'),
        ('Implementations', 'scarcity/implementations/index'),
        ('Use Cases', 'scarcity/implementations/experiments'),
        ('Limitations & Roadmap', 'scarcity/limitations'),
        ('FAQ', 'scarcity/faq'),
    ]
    resolved = []
    for title, path in sections:
        page = flatpages.get(path)
        resolved.append({
            'title': title,
            'path': path,
            'description': page.meta.get('description') if page else '',
        })
    return render_template('scarcity_hub.html', sections=resolved)

@app.route('/scarcity/overview')
def scarcity_overview():
    """Default Scarcity overview"""
    return render_flatpage('scarcity/overview')

@app.route('/scarcity/<path:subpath>')
def scarcity_page(subpath):
    """Scarcity subpages"""
    return render_flatpage(f'scarcity/{subpath}')

@app.route('/library')
@app.route('/library/')
def library_index():
    """Library landing grouped by category"""
    pages = [p for p in flatpages if p.path.startswith('library/')]
    
    grouped = {}
    for page in pages:
        parts = page.path.split('/')
        category = parts[1] if len(parts) > 1 else 'foundations'
        grouped.setdefault(category, []).append(page)

    for items in grouped.values():
        items.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)

    # Friendly ordering for the library hub
    category_order = [
        'foundations',
        'learning-paradigms',
        'systems-thinking',
        'practical-advice',
        'scarcity',
    ]
    ordered_groups = []
    for cat in category_order:
        if cat in grouped:
            ordered_groups.append((cat, grouped[cat]))
    # Add any remaining categories
    for cat, items in grouped.items():
        if cat not in category_order:
            ordered_groups.append((cat, items))

    return render_template('library_index.html', grouped=ordered_groups)

@app.route('/library/<path:subpath>')
def library_page(subpath):
    """Library detail pages"""
    return render_flatpage(f'library/{subpath}')

@app.route('/research-log')
@app.route('/research-log/')
def research_log_index():
    """Research log landing"""
    logs = [p for p in flatpages if p.path.startswith('research-log/')]
    logs.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)
    return render_template('research_log.html', logs=logs)

@app.route('/research-log/<path:subpath>')
def research_log_page(subpath):
    """Research log entries"""
    return render_flatpage(f'research-log/{subpath}')

@app.route('/writing')
@app.route('/writing/')
def writing_index():
    """Writing landing page for poetry and essays"""
    pages = [p for p in flatpages if p.path.startswith('writing/')]
    
    grouped = {}
    for p in pages:
        # Determine category from folder under writing/
        parts = p.path.split('/')
        category = parts[1] if len(parts) > 1 else 'writing'
        grouped.setdefault(category, []).append(p)

    for items in grouped.values():
        items.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)
    
    category_order = ['essays', 'poetry', 'reflections']
    ordered_groups = []
    for cat in category_order:
        if cat in grouped:
            ordered_groups.append((cat, grouped[cat]))
    for cat, items in grouped.items():
        if cat not in category_order:
            ordered_groups.append((cat, items))

    return render_template('writing.html', grouped=ordered_groups)

@app.route('/writing/<path:subpath>')
def writing_page(subpath):
    """Writing subpages"""
    return render_flatpage(f'writing/{subpath}')

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

@app.template_filter('page_url')
def page_url(path):
    """Generate proper URL for a FlatPage path"""
    # Remove .md extension if present
    if path.endswith('.md'):
        path = path[:-3]
    
    # Ensure it starts with /
    if not path.startswith('/'):
        path = '/' + path
        
    # Add trailing slash for directory-based URLs
    if not path.endswith('/'):
        path += '/'
        
    return path

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

