# GitHub Pages Website with Custom Domain

This repository contains a website hosted on GitHub Pages with a custom domain configuration.

## 🚀 Setup Instructions

### Step 1: Create GitHub Repository
1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right and select "New repository"
3. Name your repository (e.g., `my-website` or `username.github.io`)
4. Make it **Public** (required for free GitHub Pages)
5. Click "Create repository"

### Step 2: Push Your Code to GitHub
Open your terminal in this project folder and run:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git push -u origin main
```

Replace `YOUR-USERNAME` and `YOUR-REPO-NAME` with your actual GitHub username and repository name.

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Scroll down to **Pages** (left sidebar)
4. Under **Source**, select `main` branch and `/ (root)` folder
5. Click **Save**
6. GitHub will provide a URL like `https://username.github.io/repository-name/`

### Step 4: Configure Your Custom Domain

#### A. Update the CNAME File
1. Edit the `CNAME` file in this repository
2. Replace `your-domain.com` with your actual domain name (e.g., `example.com` or `www.example.com`)
3. Commit and push the change:
   ```bash
   git add CNAME
   git commit -m "Update custom domain"
   git push
   ```

#### B. Configure DNS Settings at Your Domain Registrar
You have two options:

**Option 1: Using an Apex Domain (e.g., example.com)**
1. Go to your domain registrar's DNS settings
2. Add four A records pointing to GitHub's IP addresses:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```
3. Optionally, add a CNAME record:
   - Host: `www`
   - Points to: `your-username.github.io`

**Option 2: Using a Subdomain (e.g., www.example.com)**
1. Go to your domain registrar's DNS settings
2. Add a CNAME record:
   - Host: `www` (or your chosen subdomain)
   - Points to: `your-username.github.io`

#### C. Configure Custom Domain in GitHub
1. Go to your repository's **Settings** → **Pages**
2. Under **Custom domain**, enter your domain (e.g., `example.com`)
3. Click **Save**
4. Wait a few minutes, then check **Enforce HTTPS** (recommended)

### Step 5: Wait for DNS Propagation
DNS changes can take up to 24-48 hours to propagate, but often complete within a few hours.

## 🎨 Customization

### Update Content
- Edit `index.html` to change the website content
- Modify `styles.css` to adjust the design
- Update the footer with your name and year

### Add More Pages
Create additional HTML files (e.g., `about.html`, `contact.html`) and link to them in your navigation.

## 📝 File Structure

```
.
├── index.html      # Main HTML file
├── styles.css      # Stylesheet
├── CNAME          # Custom domain configuration
├── .gitignore     # Git ignore rules
└── README.md      # This file
```

## 🔧 Troubleshooting

### Custom Domain Not Working?
- Check that DNS settings are correct at your registrar
- Verify the CNAME file contains only your domain name (no http:// or https://)
- Wait for DNS propagation (can take up to 48 hours)
- Check GitHub Pages settings show "DNS check successful"

### HTTPS Not Available?
- Wait a few minutes after DNS is configured
- GitHub automatically provisions SSL certificates via Let's Encrypt
- Make sure "Enforce HTTPS" is checked in Settings → Pages

### 404 Error?
- Ensure your repository is public
- Check that GitHub Pages is enabled
- Verify the source branch is correct (main branch, / root folder)

## 📚 Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Configuring Custom Domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Managing DNS for GitHub Pages](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)

## 📄 License

Feel free to use this template for your own website!

---

**Happy Hosting! 🎉**

