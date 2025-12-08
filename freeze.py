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
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

@freezer.register_generator
def blog_post():
    """Generate URLs for all blog posts"""
    for post in flatpages:
        # Only generate URLs for blog posts and strip the leading "blog/" prefix
        if post.path.startswith('blog/'):
            clean_path = post.path.split('blog/', 1)[1]
            yield {'path': clean_path}

@freezer.register_generator
def project_detail():
    """Generate URLs for all project detail pages"""
    # Derive project slugs from flatpages entries under portfolio/projects
    for page in flatpages:
        if page.path.startswith('portfolio/projects/') and page.path.endswith('/index'):
            slug = page.path.split('/')[-2]
            yield {'project_slug': slug}

@freezer.register_generator
def blog_category():
    """Generate URLs for all blog category pages"""
    categories = ['ai-ml', 'finance-economics', 'poetry', 'self-improvement', 'tech-concepts', 'random']
    for category in categories:
        yield {'category': category}

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
    
    # Portfolio
    sitemap.append('  <url>')
    sitemap.append(f'    <loc>{site_url}/portfolio/</loc>')
    sitemap.append(f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>')
    sitemap.append('    <changefreq>monthly</changefreq>')
    sitemap.append('    <priority>0.8</priority>')
    sitemap.append('  </url>')
    
    # Blog listing
    sitemap.append('  <url>')
    sitemap.append(f'    <loc>{site_url}/blog/</loc>')
    sitemap.append(f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>')
    sitemap.append('    <changefreq>weekly</changefreq>')
    sitemap.append('    <priority>0.9</priority>')
    sitemap.append('  </url>')
    
    # Blog posts
    for post in flatpages:
        sitemap.append('  <url>')
        sitemap.append(f'    <loc>{site_url}/blog/{post.path}</loc>')
        post_date = post.meta.get('date')
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


