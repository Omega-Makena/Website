# 🚀 GitHub Pages Deployment Guide

Your website is now ready for GitHub Pages! Here's the complete deployment guide.

---

## ✅ What's Already Set Up

✨ **Great news!** Your site is **already configured** for GitHub Pages:

- ✅ `freeze.py` - Generates static files to `docs/` folder
- ✅ `CNAME` - Custom domain configured (`omegamakena.co.ke`)
- ✅ Dynamic project system - No code editing needed
- ✅ Blog system - Markdown-based posts
- ✅ Responsive design with dark mode

---

## 📦 Step 1: Generate Static Site

Every time you make changes, run:

```bash
# Activate virtual environment
venv\Scripts\activate

# Generate static files
python freeze.py
```

This creates the `docs/` folder with your static website.

---

## 🔧 Step 2: Configure GitHub Repository

### First Time Setup

1. **Go to your repository on GitHub:**
   - Navigate to `https://github.com/Omega-Makena/Website`

2. **Go to Settings → Pages**
   - Click **Settings** at the top
   - Click **Pages** in the left sidebar

3. **Configure Source:**
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
   - Click **Save**

4. **Custom Domain (Already configured):**
   - The `CNAME` file contains: `omegamakena.co.ke`
   - This is automatically copied to `docs/` by `freeze.py`

---

## 🌐 Step 3: Configure DNS (Your Domain Registrar)

To use your custom domain `omegamakena.co.ke`, configure DNS at your domain registrar:

### Option A: Apex Domain (omegamakena.co.ke)

Add **4 A Records** pointing to GitHub's servers:

```
Type: A
Host: @
Value: 185.199.108.153

Type: A
Host: @
Value: 185.199.109.153

Type: A
Host: @
Value: 185.199.110.153

Type: A  
Host: @
Value: 185.199.111.153
```

### Option B: WWW Subdomain (www.omegamakena.co.ke)

Add a **CNAME Record**:

```
Type: CNAME
Host: www
Value: omega-makena.github.io
```

---

## 🚢 Step 4: Deploy Workflow

### Every Time You Make Changes:

```bash
# 1. Make your changes (edit config.yaml, add projects, write blog posts)

# 2. Test locally
python app.py
# Visit http://localhost:5000

# 3. Generate static files
python freeze.py

# 4. Commit and push
git add .
git commit -m "Update website content"
git push origin main

# 5. Wait 2-3 minutes for GitHub Pages to build
```

---

## 🔒 Step 5: Enable HTTPS (After DNS Propagates)

1. Wait for DNS to propagate (up to 48 hours, usually 1-2 hours)
2. Go to **Settings → Pages**
3. Check **Enforce HTTPS**
4. Your site will use Let's Encrypt SSL automatically

---

## 📁 What Gets Deployed?

The `docs/` folder contains:

```
docs/
├── index.html          # Homepage
├── portfolio/          # Portfolio page
│   └── index.html
├── blog/               # Blog pages
│   ├── index.html      # Blog listing
│   └── [post-name]/    # Individual posts
│       └── index.html
├── static/             # CSS, JS, images
│   └── img/
└── CNAME               # Custom domain configuration
```

---

## ✅ Verification Checklist

After deploying, check:

- [ ] Site loads at `https://omegamakena.co.ke`
- [ ] Homepage shows your name and bio
- [ ] Portfolio page shows projects from YAML files
- [ ] Blog page shows all blog posts
- [ ] Dark mode toggle works
- [ ] All links work correctly
- [ ] Images load properly
- [ ] Mobile responsive design works

---

## 🐛 Troubleshooting

### Site Not Loading?

**Check GitHub Pages Status:**
1. Go to **Settings → Pages**
2. Look for "Your site is live at..."
3. Check for any error messages

**Common Issues:**
- Wait 2-3 minutes after pushing
- Clear browser cache (`Ctrl+F5`)
- Check that `docs/` folder exists in your repo
- Verify branch is set to `main` and folder to `/docs`

### Custom Domain Not Working?

**DNS Issues:**
1. Verify DNS records at your registrar
2. Check DNS propagation: https://dnschecker.org
3. Wait up to 48 hours for full propagation
4. Make sure CNAME file contains only your domain

**GitHub Pages Settings:**
1. Go to **Settings → Pages**
2. Look for "DNS check successful" message
3. If not, double-check A records

### 404 Errors?

- Make sure to use trailing slashes: `/blog/` not `/blog`
- Check that files exist in `docs/` folder
- Verify `freeze.py` ran successfully

### Images Not Loading?

- Check image paths start with `/static/img/`
- Verify images exist in `static/img/`
- Check `docs/static/img/` folder after freezing

---

## 📊 GitHub Pages Limits

- **Repository size**: 1 GB recommended
- **Site size**: 1 GB soft limit
- **Bandwidth**: 100 GB per month (soft limit)
- **Builds**: 10 per hour

Your site should be well under these limits!

---

## 🎯 Quick Deploy Commands

### Initial Setup
```bash
# Generate site
python freeze.py

# Push to GitHub
git add .
git commit -m "Initial deployment"
git push origin main
```

### Regular Updates
```bash
# Quick update script
python freeze.py && git add docs && git commit -m "Update site" && git push
```

### Or use the setup script (Windows)
```bash
setup.bat
```

---

## 📞 Need Help?

### GitHub Pages Documentation
- [GitHub Pages Basics](https://docs.github.com/en/pages)
- [Custom Domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Troubleshooting](https://docs.github.com/en/pages/getting-started-with-github-pages/troubleshooting-404-errors-for-github-pages-sites)

### DNS Configuration Help
- [DNS Checker](https://dnschecker.org)
- [What's My DNS](https://www.whatsmydns.net)

---

## 🎉 You're All Set!

Your website is now:
- ✅ Fully dynamic (edit YAML files, no code)
- ✅ Deployed to GitHub Pages
- ✅ Using custom domain
- ✅ HTTPS enabled
- ✅ Optimized and fast

**Happy publishing!** 🚀

---

## 🔄 Update Workflow Summary

```
Edit files          Test locally         Generate static      Deploy
(YAML/Markdown) →   (python app.py) →   (python freeze.py) → (git push)
                    http://localhost     Creates docs/         Live site!
```

---

Need to add a project? Just create a YAML file in `projects/` and deploy!
Need to write a blog post? Add a Markdown file to `posts/` and deploy!
Need to update your bio? Edit `config.yaml` and deploy!

**No code editing required!** 🎨

