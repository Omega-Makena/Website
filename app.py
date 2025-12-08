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

@app.route('/work/')
def work():
    """Work page"""
    page = flatpages.get('work')
    if not page:
        abort(404)
    return render_template('work.html', page=page)

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
    """Library landing grouped by category"""
    pages = [p for p in flatpages if p.path.startswith('library/')]
    
    grouped = {}
    for page in pages:
        parts = page.path.split('/')
        category = parts[1] if len(parts) > 1 else 'library'
        grouped.setdefault(category, []).append(page)

    for items in grouped.values():
        items.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)

    ordered_groups = sorted(grouped.items(), key=lambda x: x[0])
    return render_template('library_index.html', grouped=ordered_groups)

@app.route('/library/<path:subpath>')
def library_page(subpath):
    """Library detail pages"""
    return render_flatpage(f'library/{subpath}')

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

@app.route('/writing/')
def writing_index():
    """Unified writing section landing"""
    content_dirs = ['library', 'research-log', 'writing']
    pages = [p for p in flatpages if p.path.startswith(tuple(f'{d}/' for d in content_dirs))]
    
    grouped = {}
    for p in pages:
        # Determine category from the top-level directory
        category = p.path.split('/')[0]
        
        # Use a more descriptive title for the category
        category_title = category.replace('-', ' ').title()
        
        # Initialize category if not present
        if category_title not in grouped:
            grouped[category_title] = []
        
        # Add page to the corresponding category
        grouped[category_title].append(p)

    # Sort pages within each category by date
    for items in grouped.values():
        items.sort(key=lambda x: x.meta.get('date', datetime.min), reverse=True)
    
    # Create a sorted list of categories to ensure consistent order
    # Example order: Research Log, Library, Writing
    category_order = ['Research Log', 'Library', 'Writing']
    ordered_groups = [(cat, grouped[cat]) for cat in category_order if cat in grouped]

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

