# 🚀 Deploy Your Website RIGHT NOW!

## ✅ Step 1: Your Code is Already Pushed! ✓

Your website files are now on GitHub at:
**https://github.com/Omega-Makena/Website**

---

## 🔧 Step 2: Configure GitHub Pages (Takes 2 Minutes!)

### Go to Your Repository Settings:

1. **Open your browser** and go to:
   ```
   https://github.com/Omega-Makena/Website
   ```

2. **Click "Settings"** (top right of the repository page)

3. **Click "Pages"** (left sidebar, under "Code and automation")

4. **Configure the source:**
   
   Under "Build and deployment":
   
   - **Source**: Select `Deploy from a branch`
   
   - **Branch**: 
     - Select `main` from the dropdown
     - Select `/docs` from the folder dropdown
     - Click **Save**

5. **Wait for the build** (30 seconds - 2 minutes)
   
   You'll see: "Your site is live at https://omega-makena.github.io/Website/"

---

## 🌐 Step 3: Configure Custom Domain (Optional)

Your CNAME file is already set to `omegamakena.co.ke`. To use it:

### At Your Domain Registrar:

Add these **4 A Records**:

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

### Back in GitHub Pages Settings:

1. Under "Custom domain", enter: `omegamakena.co.ke`
2. Click **Save**
3. Wait for DNS check (shows "DNS check successful")
4. Check **Enforce HTTPS** (after DNS propagates)

---

## 🎯 Your URLs

After GitHub Pages is configured:

- **GitHub URL**: https://omega-makena.github.io/Website/
- **Custom Domain** (after DNS): https://omegamakena.co.ke

---

## ✅ Verification

Your site should show:
- ✓ Your name and bio on homepage
- ✓ 2 projects in portfolio
- ✓ 7 blog posts in blog section
- ✓ Dark mode toggle working
- ✓ Responsive on mobile

---

## 🔄 Future Updates

Every time you make changes:

```bash
# 1. Make changes (add .md files, edit config.yaml, etc.)

# 2. Generate static site
python freeze.py

# 3. Commit and push
git add .
git commit -m "Update website"
git push origin main

# 4. Wait 1-2 minutes - site updates automatically!
```

---

## 🐛 Troubleshooting

### "Pages" tab not visible?
- Make sure repository is **Public** (not Private)
- Check you have admin access to the repository

### Build failed?
- Check Actions tab for error messages
- Verify docs/ folder exists in your repository
- Make sure .gitignore doesn't exclude docs/

### 404 Error?
- Make sure Source is set to `/docs` not `/ (root)`
- Wait 2-3 minutes after configuration
- Clear browser cache

### Custom domain not working?
- Verify DNS records at your registrar
- Check https://dnschecker.org for propagation
- Can take up to 48 hours (usually 1-2 hours)

---

## 📞 Quick Links

- **Your Repository**: https://github.com/Omega-Makena/Website
- **GitHub Pages Docs**: https://docs.github.com/en/pages
- **DNS Checker**: https://dnschecker.org

---

## 🎉 You're Almost There!

Just go to your repository settings and configure GitHub Pages. Your dynamic website will be live in minutes!

**Total time: ~2 minutes** ⏱️

