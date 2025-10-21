"""
Generate static files for GitHub Pages deployment
"""
from flask_frozen import Freezer
from app import app, flatpages
import os
import shutil

freezer = Freezer(app)

# Configure freezer
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

@freezer.register_generator
def blog_post():
    """Generate URLs for all blog posts"""
    for post in flatpages:
        yield {'path': post.path}

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
    
    print("✅ Static site generated in 'docs' folder!")
    print("📁 Ready to deploy to GitHub Pages")


