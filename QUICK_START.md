# 📊 Regional Science Dashboard - Quick Start

Your interactive dashboard is ready! Here's what has been created for you:

## ✅ What's Included

### Files Created
- **app.py** - Main Streamlit dashboard application
- **requirements.txt** - Python dependencies
- **README.md** - Comprehensive documentation
- **DEPLOYMENT.md** - Step-by-step deployment guide
- **.gitignore** - Git configuration
- Git repository initialized and ready

### Data
- **topfield_lowdiff_pubs.csv** - 931 publications with citation metrics
- **Dimensions-Publication-2026-07-05_23-24-23.xlsx** - Publication metadata

## 🎯 Dashboard Features

### Filters
- ✅ Publication year range
- ✅ Field of study (multi-select)
- ✅ Author region group (multi-select)
- ✅ Minimum citation threshold
- ✅ Own-region citation share threshold

### Visualizations
- ✅ Publications over time
- ✅ Citations over time
- ✅ Publications by field
- ✅ Citations by field
- ✅ Publications by region
- ✅ Region citation share patterns
- ✅ Citations vs diffusion scatter plot

### Data Browser
- ✅ Filterable table of all publications
- ✅ Individual publication detail view with:
  - Full title and abstract
  - Citation metrics and regional breakdown
  - DOI link to full publication
  - Journal/source information

## 🚀 Next Steps

### Option A: Test Locally (Before Publishing)
```bash
cd "/Users/randolyao/MIT Dropbox/Randol Yao/science_geo/tmpdata/dashboard"
streamlit run app.py
```
Then open http://localhost:8501 in your browser to test.

### Option B: Deploy to Streamlit Cloud (Recommended for Sharing)

1. **Create a GitHub account** (if you don't have one)
2. **Create a new repository** at github.com (name it something like `regional-science-dashboard`)
3. **Push your code**:
   ```bash
   cd "/Users/randolyao/MIT Dropbox/Randol Yao/science_geo/tmpdata/dashboard"
   git remote add origin https://github.com/YOUR_USERNAME/regional-science-dashboard.git
   git push -u origin main
   ```
4. **Deploy to Streamlit Cloud**:
   - Go to https://share.streamlit.io
   - Click "New app"
   - Select your repository, branch (main), and main file (app.py)
   - Click Deploy
   - Get a public link like: `https://your-app-name.streamlit.app`

**That's it!** Your dashboard is live and shareable. ✨

## 📋 Key Metrics

The dashboard displays:
- **Total Publications**: 931 high-impact publications
- **Citation Range**: From ~50 to 1000+ citations
- **Geographic Coverage**: 5 regions (China, US, EU, and others)
- **Field Coverage**: Multiple scientific disciplines
- **Time Period**: Publications from various years

## 💡 Tips for Users

- **Narrow down**: Use filters to find specific combinations (e.g., publications from China in 2020+)
- **Hover over charts**: Get detailed numbers by hovering over visualizations
- **Sort tables**: Click column headers in the data table to sort
- **Read abstracts**: Select a publication to see full details and external links
- **Export data**: Screenshot or copy tables as needed

## 🔄 Updating the Dashboard

To update with new data or modify the dashboard:

1. Edit `app.py` or update data files
2. Commit changes: `git add . && git commit -m "Description"`
3. Push to GitHub: `git push origin main`
4. Streamlit Cloud automatically redeploys (~1-2 minutes)

## 📞 Support

Refer to the complete guides:
- **README.md** - Full documentation and methodology
- **DEPLOYMENT.md** - Detailed deployment instructions
- **app.py** - Code comments explaining functionality

---

**You're all set!** Your dashboard is ready to share with colleagues and research partners. 🌍
