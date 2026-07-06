# 🚀 Deployment Guide - Streamlit Cloud

This dashboard is ready to deploy on **Streamlit Cloud** (free tier available). Follow these steps to get it live and shareable.

## Step 1: Create a GitHub Repository

1. Go to [github.com](https://github.com) and sign in (or create an account if needed)
2. Click the **+** icon → **New repository**
3. Name it something like `regional-science-dashboard`
4. Leave it public (required for free Streamlit Cloud)
5. Click **Create repository**

## Step 2: Push Your Code to GitHub

Replace `USERNAME` with your GitHub username and run:

```bash
cd "/Users/randolyao/MIT Dropbox/Randol Yao/science_geo/tmpdata/dashboard"

# Add the remote
git remote add origin https://github.com/USERNAME/regional-science-dashboard.git
git branch -M main

# Push the code
git push -u origin main
```

⚠️ **First time setup**: If git asks for credentials:
- Use your GitHub username
- For password, create a [Personal Access Token](https://github.com/settings/tokens) with `repo` scope and paste that instead

## Step 3: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **New app**
3. Select:
   - **Repository**: `USERNAME/regional-science-dashboard`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Click **Deploy!**

Streamlit will take ~2-3 minutes to build and deploy. You'll get a shareable link like:
```
https://regional-science-dashboard-USERNAME.streamlit.app
```

## Step 4: Share Your Dashboard

Once deployed, you can share the link with anyone! The dashboard works in any web browser, no installation needed.

### Tips for Sharing
- The dashboard is interactive and responds instantly to filter changes
- Mobile-friendly responsive design
- Works best in Chrome, Firefox, Safari, or Edge

## Updating the Dashboard

To update the dashboard with new data or code changes:

1. Make your changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update: [description of changes]"
   git push origin main
   ```
3. Streamlit Cloud will automatically redeploy within 1-2 minutes

## Using a Different Data Source

If you update the data files later:

1. Replace `topfield_lowdiff_pubs.csv` and/or `Dimensions-Publication-2026-07-05_23-24-23.xlsx` 
2. Commit and push:
   ```bash
   git add topfield_lowdiff_pubs.csv Dimensions-Publication-2026-07-05_23-24-23.xlsx
   git commit -m "Update: Refresh data to latest version"
   git push origin main
   ```

## Troubleshooting

### "Module not found" errors
- Ensure `requirements.txt` is in the root directory with all dependencies listed
- Make sure all imports in `app.py` are in `requirements.txt`

### Data files not loading
- Verify both CSV and XLSX files are in the repository root directory
- Check file paths in `app.py` are relative paths (not absolute paths)
- Git the data files and push them to GitHub

### App loads slowly
- First load takes 2-3 seconds (cached after that)
- Large datasets may take 5-10 seconds on first run
- Streamlit Cloud has free tier resources; paid tiers have better performance

### Want more control?
Consider deploying to:
- **Heroku** (requires credit card, has free tier limits)
- **Railway** (similar to Heroku)
- **Replit** (simple alternative)
- **AWS/GCP/Azure** (more complex but fully customizable)

---

**That's it!** Your interactive dashboard is now live and shareable. 🎉
