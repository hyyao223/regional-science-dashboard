# 🌍 Regional Science Dashboard

An interactive dashboard for exploring highly-cited publications with strong geographic focus. This dashboard helps researchers understand how top-tier research is distributed across regions and identify publications that are influential within specific geographic areas but have limited diffusion to other regions.

## 📊 About the Data

This dashboard analyzes 931 publications that meet three criteria:
- **Top 0.1%** by normalized citation count (normalized by field and publication year)
- **Regional concentration**: Authors from the same geographic region
- **Limited diffusion**: Own-region citation share > 50%

### Data Sources
- **topfield_lowdiff_pubs.csv** - Main dataset with citation metrics and regional data
- **Dimensions-Publication-2026-07-05_23-24-23.xlsx** - Supplementary publication metadata (titles, abstracts, DOIs, etc.)

## 🎯 Features

### Interactive Filters
- **Publication Year**: Filter by year range
- **Field of Study**: Browse by research discipline
- **Author Region Group**: Filter by geographic region
- **Citation Threshold**: Set minimum citation count
- **Regional Focus**: Adjust own-region citation share threshold

### Visualizations
- **Distribution over time**: Publications and citations by year
- **Field analysis**: Publications and citation metrics by field
- **Regional analysis**: Publications and citation patterns by region
- **Citation vs Diffusion**: Scatter plot showing relationship between citation count and regional focus

### Publication Details
- **Filterable table**: Browse all matching publications with key metrics
- **Detailed view**: Select any publication to see:
  - Full title and abstract
  - Citation metrics (total citations and regional distribution)
  - DOI link to the full publication
  - Publication source (journal/venue)

## 🚀 Running Locally

### Requirements
- Python 3.8+
- Dependencies in `requirements.txt`

### Setup
```bash
pip install -r requirements.txt
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`

## 🌐 Deployed Version

This dashboard is hosted on [Streamlit Cloud](https://streamlit.io/cloud) for easy sharing.

## 📝 Data Methodology

Publications were selected based on:
1. **Citation normalization**: Citations normalized by field and publication year to ensure fair cross-field comparison
2. **Regional filtering**: Only publications where all authors are from the same region
3. **Geographic concentration**: Only publications where >50% of citations come from the author's region
4. **Top performance**: Only top 0.1% of publications by normalized citation count within each field

This methodology identifies impactful research that is highly cited but primarily within its own geographic region.

## 📧 Contact & Questions

For questions about this dashboard or the underlying data, please reach out.

---

**Last Updated**: July 5, 2026
