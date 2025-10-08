# 🚀 Deployment Guide

This guide will help you deploy your portfolio website to GitHub Pages.

## Quick Start (5 minutes)

### Step 1: Create GitHub Repository
1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository: `portfolio` or `your-username.github.io`
5. Make it **Public** (required for free GitHub Pages)
6. Click "Create repository"

### Step 2: Upload Your Files
1. In your new repository, click "uploading an existing file"
2. Drag and drop all files from your portfolio folder:
   - `index.html`
   - `README.md`
   - `assets/` folder (with all subfolders)
3. Add a commit message: "Initial portfolio website"
4. Click "Commit changes"

### Step 3: Enable GitHub Pages
1. Go to your repository **Settings**
2. Scroll down to "Pages" section (left sidebar)
3. Under "Source", select "Deploy from a branch"
4. Choose "main" branch and "/ (root)" folder
5. Click "Save"

### Step 4: Access Your Website
- Your site will be live at: `https://your-username.github.io/portfolio`
- If you named your repo `your-username.github.io`, it will be at: `https://your-username.github.io`
- GitHub Pages may take 5-10 minutes to deploy initially

## 🎯 Custom Domain (Optional)

If you have a custom domain:

1. In repository Settings → Pages
2. Add your domain in "Custom domain" field
3. Create a `CNAME` file in your repository root:
   ```
   your-domain.com
   ```
4. Update your DNS settings to point to GitHub Pages

## 📝 Before You Deploy

Make sure to update these files with your actual content:

### Required Updates:
- [ ] Add your profile picture: `assets/images/profile.jpg`
- [ ] Add project images: `assets/images/projects/*.jpg`
- [ ] Add your resume: `assets/docs/resume.pdf`
- [ ] Update contact information in `index.html`
- [ ] Update social media links in `index.html`
- [ ] Create project case studies in `assets/docs/projects/`

### Optional Updates:
- [ ] Update the Formspree form ID in the contact section
- [ ] Customize colors and styling
- [ ] Add more projects or sections

## 🔧 Troubleshooting

### Common Issues:

**404 Error on GitHub Pages:**
- Ensure your repository is public
- Check that GitHub Pages is enabled in Settings
- Wait 10-15 minutes for initial deployment

**Images Not Loading:**
- Verify image file paths are correct
- Check file extensions (case-sensitive)
- Ensure images are uploaded to the correct folders

**Contact Form Not Working:**
- Update the Formspree form ID in `index.html`
- Test the form after deployment

**Styling Issues:**
- Check browser console for errors
- Ensure all external CDN links are accessible
- Verify Tailwind CSS is loading properly

## 📱 Testing Your Site

Before sharing your portfolio:

1. **Desktop Testing:**
   - Chrome, Firefox, Safari, Edge
   - Different screen sizes (1920x1080, 1366x768)

2. **Mobile Testing:**
   - Test on actual mobile devices
   - Use browser dev tools mobile emulation
   - Check touch interactions and scrolling

3. **Performance Testing:**
   - Use Google PageSpeed Insights
   - Check loading times on slow connections
   - Optimize images if needed

## 🎉 You're Done!

Your portfolio is now live and ready to impress potential employers and clients!

**Next Steps:**
- Share your portfolio URL on LinkedIn
- Add it to your resume
- Include it in job applications
- Keep it updated with new projects

---

**Need Help?** Check the main README.md for detailed documentation.


