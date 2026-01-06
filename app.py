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
app.config['FLATPAGES_EXCLUDE'] = ['venv', '.venv', 'node_modules', '.git', 'docs', 'site', '__pycache__']


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

@app.template_filter('format_date')
def format_date(value):
    """Format date for display, handling string, date, and datetime"""
    if not value:
        return ''
        
    date_obj = value
    
    # If string, parse it
    if isinstance(value, str):
        try:
            date_obj = datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            return value
            
    # If it's a date but not a datetime (time is 00:00), convert or just format
    # Note: datetime is a subclass of date, so isinstance(dt, date) is True.
    # We can just check for .strftime method.
    if hasattr(date_obj, 'strftime'):
        return date_obj.strftime('%B %d, %Y')
        
    return value

def get_page_date(page):
    """Extract date from page meta and ensure it is a datetime object for sorting"""
    d = page.meta.get('date', datetime.min)
    if isinstance(d, str):
        try:
            d = datetime.strptime(d, '%Y-%m-%d')
        except ValueError:
            return datetime.min
    # Convert datetime.date to datetime.datetime if needed
    if not isinstance(d, datetime) and hasattr(d, 'timetuple'):
        # datetime.date to datetime.datetime
        d = datetime.combine(d, datetime.min.time())
    return d

@app.route('/')
def index():
    """Home / Command Center"""
    all_content = []
    
    # Research Logs
    for p in flatpages:
        if p.path.startswith('research-log/'):
            p.meta['type'] = 'LOG'
            all_content.append(p)
        elif p.path.startswith('library/'):
            p.meta['type'] = 'LIBRARY'
            all_content.append(p)
        elif p.path.startswith('writing/'):
            p.meta['type'] = 'ESSAY'
            all_content.append(p)
            
    # Sort by date
    all_content.sort(key=get_page_date, reverse=True)
    
    # Get top 6
    feed_items = all_content[:6]

    return render_template(
        'index.html',
        feed_items=feed_items
    )

@app.route('/lab-notes/')
def lab_notes():
    """The Lab Notes Archive (grouped)"""
    grouped = {
        'essays': [],
        'logs': [],
        'library': []
    }
    
    for p in flatpages:
        if p.path.startswith('writing/'):
            p.meta['type'] = 'ESSAY'
            grouped['essays'].append(p)
        elif p.path.startswith('research-log/'):
            p.meta['type'] = 'LOG'
            grouped['logs'].append(p)
        elif p.path.startswith('library/'):
            p.meta['type'] = 'LIBRARY'
            grouped['library'].append(p)
            
    # Sort each bucket
    for key in grouped:
        grouped[key].sort(key=get_page_date, reverse=True)
    
    return render_template('lab_notes.html', grouped=grouped)

@app.route('/about/')
def about():
    """About page (Bento Grid)"""
    return render_template('about.html')

@app.route('/work-with-me/')
def work_with_me():
    """Collaboration page"""
    return render_template('work_with_me.html')

@app.route('/work/')
def work():
    """Work page"""
    page = flatpages.get('work')
    if not page:
        abort(404)
    return render_template('work.html', page=page)

# Global Scarcity Sections for Navigation
SCARCITY_SECTIONS = [
    ('Overview', 'scarcity/overview'),
    ('Architecture', 'scarcity/architecture'),
    ('Core Components', 'scarcity/components'),
    ('Engine (MPIE)', 'scarcity/engine'),
    ('Federation', 'scarcity/federation'),
    ('Meta-Learning', 'scarcity/meta_learning'),
    ('Simulation', 'scarcity/simulation'),
    ('Resource Governor', 'scarcity/drg'),
    ('Stream Processing', 'scarcity/stream'),
    ('Runtime System', 'scarcity/runtime'),
    ('FMI', 'scarcity/fmi'),
    ('Math Foundations', 'scarcity/math'),
    ('API Reference', 'scarcity/api'),
    ('Implementation', 'scarcity/implementation'),
]

@app.route('/scarcity/')
def scarcity_hub():
    """Scarcity hub page"""
    resolved = []
    for title, path in SCARCITY_SECTIONS:
        page = flatpages.get(path)
        resolved.append({
            'title': title,
            'path': path,
            'description': page.meta.get('description') if page else '',
        })
    return render_template('scarcity_hub.html', sections=resolved)

@app.route('/scarcity/overview/')
def scarcity_overview():
    """Default Scarcity overview"""
    return render_flatpage('scarcity/overview')

@app.route('/scarcity/<path:subpath>/')
def scarcity_page(subpath):
    """Scarcity subpages"""
    return render_flatpage(f'scarcity/{subpath}')



def render_flatpage(path):
    """Render a FlatPages entry with contextual sidebar"""
    page = flatpages.get(path)
    if not page:
        abort(404)
        
    sidebar_items = []
    sidebar_title = ""
    back_label = "Back to Home"
    back_url = "/"
    
    # context: Scarcity
    if path.startswith('scarcity/'):
        sidebar_title = "Framework Manual"
        back_label = "← Back to Project"
        back_url = "/scarcity/"
        # Format for sidebar: (Title, URL)
        for title, p_path in SCARCITY_SECTIONS:
            sidebar_items.append({
                'title': title,
                'url': page_url(p_path),
                'active': p_path == path
            })
            
    # context: Research Log
    elif path.startswith('research-log/'):
        sidebar_title = "Recent Logs"
        back_label = "← Back to Lab Notes"
        back_url = "/lab-notes/"
        # Get last 5 logs
        logs = [p for p in flatpages if p.path.startswith('research-log/')]
        logs.sort(key=get_page_date, reverse=True)
        for p in logs[:5]:
            sidebar_items.append({
                'title': p.meta.get('title', 'Untitled'),
                'url': page_url(p.path),
                'active': p.path == path
            })

    # context: Writing
    elif path.startswith('writing/'):
        sidebar_title = "Recent Essays"
        back_label = "← Back to Lab Notes"
        back_url = "/lab-notes/"
        essays = [p for p in flatpages if p.path.startswith('writing/')]
        essays.sort(key=get_page_date, reverse=True)
        for p in essays[:5]:
            sidebar_items.append({
                'title': p.meta.get('title', 'Untitled'),
                'url': page_url(p.path),
                'active': p.path == path
            })

    return render_template('page.html', page=page, sidebar_title=sidebar_title, sidebar_items=sidebar_items, back_label=back_label, back_url=back_url)

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
        items.sort(key=get_page_date, reverse=True)

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

@app.route('/library/<path:subpath>/')
def library_page(subpath):
    """Library detail pages"""
    return render_flatpage(f'library/{subpath}')

@app.route('/research-log/')
def research_log_index():
    """Research log landing"""
    logs = [p for p in flatpages if p.path.startswith('research-log/')]
    logs.sort(key=get_page_date, reverse=True)
    return render_template('research_log.html', logs=logs)

@app.route('/research-log/<path:subpath>/')
def research_log_page(subpath):
    """Research log entries"""
    return render_flatpage(f'research-log/{subpath}')

@app.route('/writing/')
def writing_index():
    """Writing landing page for poetry and essays"""
    pages = [p for p in flatpages if p.path.startswith('writing/')]
    
    grouped = {}
    for p in pages:
        # Determine category from folder under writing/
        parts = p.path.split('/')
        if len(parts) > 1 and parts[1] in ['essays', 'poetry', 'reflections']:
            category = parts[1]
            grouped.setdefault(category, []).append(p)

    for items in grouped.values():
        items.sort(key=get_page_date, reverse=True)
    
    category_order = ['essays', 'poetry', 'reflections']
    ordered_groups = []
    for cat in category_order:
        if cat in grouped:
            ordered_groups.append((cat, grouped[cat]))
    
    # Add any remaining categories that might not be in the predefined order
    for cat, items in grouped.items():
        if cat not in category_order:
            ordered_groups.append((cat, items))

    return render_template('writing.html', grouped=ordered_groups)

@app.route('/writing/<path:subpath>/')
def writing_page(subpath):
    """Writing subpages"""
    return render_flatpage(f'writing/{subpath}')

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

