"""
Generate static files for GitHub Pages deployment
"""
from flask_frozen import Freezer
from app import app, flatpages, SITE_CONFIG
import os
import shutil
from datetime import datetime

freezer = Freezer(app)

# Configure freezer
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = False
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_STATIC_IGNORE'] = ['*.md', '*.pyc', '__pycache__']

@freezer.register_generator
def index():
    """Home page"""
    yield {}

@freezer.register_generator
def scarcity_hub():
    """Scarcity hub page"""
    yield {}

@freezer.register_generator
def scarcity_overview():
    """Scarcity overview page"""
    yield {}

@freezer.register_generator
def library_index():
    """Library index page"""
    yield {}

@freezer.register_generator
def research_log_index():
    """Research log index page"""
    yield {}

@freezer.register_generator
def writing_index():
    """Writing index page"""
    yield {}

@freezer.register_generator
def work():
    """Work page"""
    yield {}

@freezer.register_generator
def work_with_me():
    """Work with me page"""
    yield {}

@freezer.register_generator
def about():
    """About page"""
    yield {}

@freezer.register_generator
def scarcity_page():
    """Scarcity subpages"""
    for page in flatpages:
        if page.path.startswith('scarcity/') and page.path != 'scarcity/overview':
            subpath = page.path.split('scarcity/', 1)[1]
            yield {'subpath': subpath}

@freezer.register_generator
def library_page():
    """Library detail pages"""
    for page in flatpages:
        if page.path.startswith('library/'):
            subpath = page.path.split('library/', 1)[1]
            yield {'subpath': subpath}

@freezer.register_generator
def research_log_page():
    """Research log entries"""
    for page in flatpages:
        if page.path.startswith('research-log/'):
            subpath = page.path.split('research-log/', 1)[1]
            yield {'subpath': subpath}

@freezer.register_generator
def writing_page():
    """Writing subpages"""
    for page in flatpages:
        if page.path.startswith('writing/'):
            subpath = page.path.split('writing/', 1)[1]
            yield {'subpath': subpath}

def generate_sitemap():
    """Generate sitemap.xml for search engines"""
    site_url = SITE_CONFIG.get('site', {}).get('url', 'https://omegamakena.co.ke')
    if site_url.endswith('/'):
        site_url = site_url[:-1]
    
    # Start sitemap
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    # Homepage
    sitemap.append('  <url>')
    sitemap.append(f'    <loc>{site_url}/</loc>')
    sitemap.append(f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>')
    sitemap.append('    <changefreq>weekly</changefreq>')
    sitemap.append('    <priority>1.0</priority>')
    sitemap.append('  </url>')
    
    static_paths = [
        ('/scarcity', 'monthly', '0.9'),
        ('/scarcity/overview', 'monthly', '0.9'),
        ('/library', 'weekly', '0.8'),
        ('/research-log', 'weekly', '0.85'),
        ('/writing', 'monthly', '0.7'),
        ('/about', 'yearly', '0.6'),
        ('/work-with-me', 'monthly', '0.75'),
        ('/work', 'monthly', '0.7'),
    ]

    for path, changefreq, priority in static_paths:
        sitemap.append('  <url>')
        sitemap.append(f'    <loc>{site_url}{path}</loc>')
        sitemap.append(f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>')
        sitemap.append(f'    <changefreq>{changefreq}</changefreq>')
        sitemap.append(f'    <priority>{priority}</priority>')
        sitemap.append('  </url>')

    # FlatPages entries
    for page in flatpages:
        # Skip overview as it's already in static_paths
        if page.path == 'scarcity/overview':
            continue
        loc = f'{site_url}/{page.path}'
        sitemap.append('  <url>')
        sitemap.append(f'    <loc>{loc}</loc>')
        post_date = page.meta.get('date')
        if not post_date:
            post_date = datetime.now()
        if isinstance(post_date, str):
            sitemap.append(f'    <lastmod>{post_date}</lastmod>')
        else:
            date_str = post_date.strftime("%Y-%m-%d")
            sitemap.append(f'    <lastmod>{date_str}</lastmod>')
        sitemap.append('    <changefreq>monthly</changefreq>')
        sitemap.append('    <priority>0.7</priority>')
        sitemap.append('  </url>')
    
    sitemap.append('</urlset>')
    
    # Write sitemap
    with open('docs/sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sitemap))

def generate_robots_txt():
    """Generate robots.txt for search engines"""
    site_url = SITE_CONFIG.get('site', {}).get('url', 'https://omegamakena.co.ke')
    if site_url.endswith('/'):
        site_url = site_url[:-1]
    
    robots = [
        'User-agent: *',
        'Allow: /',
        '',
        f'Sitemap: {site_url}/sitemap.xml'
    ]
    
    with open('docs/robots.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(robots))

def create_directories():
    """Create directories for nested pages"""
    for page in flatpages:
        # The path for the directory that will hold index.html
        # e.g. for page.path 'a/b/c', we need directory 'docs/a/b/c'
        directory = os.path.join(app.config['FREEZER_DESTINATION'], page.path)
        # Create directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

if __name__ == '__main__':
    # Clean old build thoroughly
    if os.path.exists('docs'):
        import time
        try:
            shutil.rmtree('docs', ignore_errors=True)
            time.sleep(0.5)  # Give filesystem time to clean up
        except Exception as e:
            print(f"Warning: Could not fully clean docs folder: {e}")
            print("Continuing anyway...")
    
    # Create directories for nested pages
    create_directories()
    
    # Generate static files
    try:
        freezer.freeze()
    except Exception as e:
        print(f"Error during freeze: {e}")
        print("Retrying with fresh docs folder...")
        if os.path.exists('docs'):
            shutil.rmtree('docs', ignore_errors=True)
        # Create directories again after cleaning
        create_directories()
        freezer.freeze()
    
    # Copy CNAME file to docs folder for custom domain
    if os.path.exists('CNAME'):
        shutil.copy('CNAME', 'docs/CNAME')
    
    # Generate sitemap.xml for SEO
    generate_sitemap()
    
    # Generate robots.txt for SEO
    generate_robots_txt()
    
    print("Static site generated in 'docs' folder!")
    print("Sitemap created for search engines")
    print("robots.txt created")
    print("Ready to deploy to GitHub Pages")
