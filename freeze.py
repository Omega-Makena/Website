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

@freezer.register_generator
def flatpage_routes():
    """
    Map FlatPages paths to their Flask routes for freezing.
    """
    for page in flatpages:
        path = page.path
        if path == 'about':
            yield 'about', {}
        elif path == 'work-with-me':
            yield 'work_with_me', {}
        elif path == 'work':
            yield 'work', {}
        elif path.startswith('scarcity/'):
            yield 'scarcity_page', {'subpath': path.split('scarcity/', 1)[1]}
        elif path.startswith('library/'):
            yield 'library_page', {'subpath': path.split('library/', 1)[1]}
        elif path.startswith('research-log/'):
            yield 'research_log_page', {'subpath': path.split('research-log/', 1)[1]}
        elif path.startswith('writing/'):
            yield 'writing_page', {'subpath': path.split('writing/', 1)[1]}

@freezer.register_generator
def static_routes():
    """Static top-level routes."""
    yield 'index', {}
    yield 'scarcity_overview', {}
    yield 'library_index', {}
    yield 'research_log_index', {}
    yield 'writing_index', {}
    yield 'work_with_me', {}
    yield 'work', {}
    yield 'about', {}

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
        ('/scarcity/overview', 'monthly', '0.9'),
        ('/library/', 'weekly', '0.8'),
        ('/research-log/', 'weekly', '0.85'),
        ('/writing/', 'monthly', '0.7'),
        ('/about/', 'yearly', '0.6'),
        ('/work-with-me/', 'monthly', '0.75'),
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
        loc = f'{site_url}/{page.path}'
        sitemap.append('  <url>')
        sitemap.append(f'    <loc>{loc}</loc>')
        post_date = page.meta.get('date')
        if not post_date:
            post_date = datetime.now()
        if isinstance(post_date, str):
            sitemap.append(f'    <lastmod>{post_date}</lastmod>')
        else:
            sitemap.append(f'    <lastmod>{post_date.strftime("%Y-%m-%d")}</lastmod>')
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
    
    # Generate static files
    try:
        freezer.freeze()
    except Exception as e:
        print(f"Error during freeze: {e}")
        print("Retrying with fresh docs folder...")
        if os.path.exists('docs'):
            shutil.rmtree('docs', ignore_errors=True)
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


