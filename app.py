import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import altair as alt

# Page config
st.set_page_config(
    page_title="Regional Science Dashboard",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌍 High-Impact, Region-Focused Publications")
st.markdown("""
Exploring publications in the top 0.1% by normalized citations that maintain strong regional focus
(own-region citation share > 75%). This dashboard helps identify highly influential research
concentrated within specific geographic regions.
""")

ANZSRC_FIELD_NAMES = {
    30: "History of Sciences",
    31: "Philosophy & History",
    32: "Cultural Studies",
    33: "Anthropology",
    34: "History of Sciences",
    35: "Human Geography",
    36: "Archaeology",
    37: "Geography",
    38: "Indigenous Studies",
    39: "Interdisciplinary Geography",
    40: "Physical Geography",
    41: "Urban & Regional Planning",
    42: "Creative Arts & Writing",
    43: "Language & Communication",
    44: "Linguistics",
    45: "Literature",
    46: "Philosophy",
    47: "Religion & Religious Studies",
    48: "English Language & Literature",
    49: "Literature Studies",
    50: "Asian-Pacific Languages",
    51: "Language & Culture Studies",
    52: "Social Sciences"
}

@st.cache_data
def load_data():
    # Load pre-merged dataset
    df = pd.read_csv('publications_data.csv')

    # Map numeric field codes to field names
    df['FieldName'] = df['SelectedField'].map(ANZSRC_FIELD_NAMES)

    return df

# Load data
try:
    df = load_data()
    st.success(f"✅ Loaded {len(df)} publications")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Sidebar filters
st.sidebar.header("📊 Filters")

# Year range
min_year = int(df['PubYear'].min())
max_year = int(df['PubYear'].max())
year_range = st.sidebar.slider(
    "Publication Year",
    min_year, max_year,
    (min_year, max_year),
    step=1
)

# Field filter
fields = sorted(df['FieldName'].unique())
selected_fields = st.sidebar.multiselect(
    "Field of Study",
    fields,
    default=fields
)

# Region filter
regions = sorted(df['region_group'].unique())
selected_regions = st.sidebar.multiselect(
    "Author Region Group",
    regions,
    default=regions
)

# Citation threshold
min_citations = st.sidebar.slider(
    "Minimum Times Cited",
    int(df['Timescited'].min()),
    int(df['Timescited'].max()),
    int(df['Timescited'].min())
)

# Own-region citation share
min_own_share = st.sidebar.slider(
    "Minimum Own-Region Citation Share",
    0.5, 1.0,
    0.5,
    step=0.05
)

# Apply filters
df_filtered = df[
    (df['PubYear'] >= year_range[0]) &
    (df['PubYear'] <= year_range[1]) &
    (df['FieldName'].isin(selected_fields)) &
    (df['region_group'].isin(selected_regions)) &
    (df['Timescited'] >= min_citations) &
    (df['own_region_cite_share'] >= min_own_share)
].copy()

st.sidebar.metric(
    "Publications Matching Filters",
    len(df_filtered),
    f"of {len(df)} total"
)

# Metrics row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Publications", len(df_filtered))
with col2:
    st.metric("Avg Citations", f"{df_filtered['Timescited'].mean():.1f}")
with col3:
    st.metric("Avg Own-Region Share", f"{df_filtered['own_region_cite_share'].mean():.1%}")
with col4:
    st.metric("Fields Covered", df_filtered['FieldName'].nunique())

# Visualizations
st.header("📈 Visualizations")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Distribution by Year", "By Field", "By Region", "Citation vs Diffusion", "Data Table"]
)

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        # Publications by year
        pubs_by_year = df_filtered.groupby('PubYear').size().reset_index(name='Count')
        fig_year = px.bar(
            pubs_by_year,
            x='PubYear',
            y='Count',
            title='Publications by Year',
            labels={'PubYear': 'Publication Year', 'Count': 'Number of Publications'},
            color='Count',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig_year, width="stretch")

    with col2:
        # Average citations by year
        avg_cites_year = df_filtered.groupby('PubYear')['Timescited'].mean().reset_index()
        fig_cites = px.line(
            avg_cites_year,
            x='PubYear',
            y='Timescited',
            title='Average Citations Over Time',
            labels={'PubYear': 'Publication Year', 'Timescited': 'Average Times Cited'},
            markers=True
        )
        st.plotly_chart(fig_cites, width="stretch")

with tab2:
    col1, col2 = st.columns(2)

    with col1:
        # By field
        field_data = df_filtered.groupby('FieldName').agg({
            'PublicationID': 'count',
            'Timescited': 'mean'
        }).reset_index()
        field_data.columns = ['Field', 'Count', 'Avg Citations']
        field_data = field_data.sort_values('Count', ascending=True)

        fig_field = px.bar(
            field_data,
            y='Field',
            x='Count',
            orientation='h',
            title='Publications by Field',
            labels={'Count': 'Number of Publications'}
        )
        st.plotly_chart(fig_field, width="stretch")

    with col2:
        fig_field_cites = px.bar(
            field_data.sort_values('Avg Citations', ascending=True),
            y='Field',
            x='Avg Citations',
            orientation='h',
            title='Average Citations by Field',
            color='Avg Citations',
            color_continuous_scale='RdYlGn'
        )
        st.plotly_chart(fig_field_cites, width="stretch")

with tab3:
    col1, col2 = st.columns(2)

    with col1:
        region_data = df_filtered.groupby('region_group').agg({
            'PublicationID': 'count',
            'Timescited': 'mean'
        }).reset_index()
        region_data.columns = ['Region', 'Count', 'Avg Citations']
        region_data = region_data.sort_values('Count', ascending=True)

        fig_region = px.bar(
            region_data,
            y='Region',
            x='Count',
            orientation='h',
            title='Publications by Region',
            color='Avg Citations',
            color_continuous_scale='Plasma'
        )
        st.plotly_chart(fig_region, width="stretch")

    with col2:
        # Own-region share by region
        share_data = df_filtered.groupby('region_group')['own_region_cite_share'].mean().reset_index()
        share_data.columns = ['Region', 'Avg Own-Region Share']
        share_data = share_data.sort_values('Avg Own-Region Share', ascending=True)

        fig_share = px.bar(
            share_data,
            y='Region',
            x='Avg Own-Region Share',
            orientation='h',
            title='Average Own-Region Citation Share',
            color='Avg Own-Region Share',
            color_continuous_scale='Blues'
        )
        fig_share.update_xaxes(type="linear", range=[0.75, 1.0])
        st.plotly_chart(fig_share, width="stretch")

with tab4:
    # Scatter: citations vs own-region share
    fig_scatter = px.scatter(
        df_filtered,
        x='own_region_cite_share',
        y='Timescited',
        color='region_group',
        size='Timescited',
        hover_data=['PubYear', 'FieldName', 'Sourcetitle'],
        title='Citations vs Own-Region Citation Share',
        labels={
            'own_region_cite_share': 'Own-Region Citation Share',
            'Timescited': 'Times Cited'
        }
    )
    fig_scatter.update_yaxes(type="log")
    st.plotly_chart(fig_scatter, width="stretch")

with tab5:
    st.subheader("📋 Publication Details")

    # Display table
    display_cols = ['PublicationID', 'Title', 'PubYear', 'FieldName', 'region_group',
                    'Timescited', 'own_region_cite_share', 'Sourcetitle']

    # Ensure columns exist
    available_cols = [col for col in display_cols if col in df_filtered.columns]

    df_display = df_filtered[available_cols].copy()
    df_display.columns = ['ID', 'Title', 'Year', 'Field', 'Region', 'Citations', 'Own-Region %', 'Source']
    df_display['Own-Region %'] = df_display['Own-Region %'].apply(lambda x: f'{x:.1%}')

    # Interactive table with sorting
    st.dataframe(
        df_display.sort_values('Citations', ascending=False),
        width="stretch",
        height=400
    )

# Detailed publication view
st.header("🔍 Publication Details")

if len(df_filtered) > 0:
    # Select a publication
    pub_options = [f"{row['Title'][:80]}..." if len(row['Title']) > 80 else row['Title']
                   for _, row in df_filtered.iterrows()]
    selected_pub_idx = st.selectbox(
        "Select a publication to view details:",
        range(len(df_filtered)),
        format_func=lambda i: pub_options[i]
    )

    selected_pub = df_filtered.iloc[selected_pub_idx]

    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader(selected_pub['Title'])

        # Metadata
        meta_col1, meta_col2, meta_col3, meta_col4 = st.columns(4)
        with meta_col1:
            st.metric("Year", int(selected_pub['PubYear']))
        with meta_col2:
            st.metric("Citations", int(selected_pub['Timescited']))
        with meta_col3:
            st.metric("Field", selected_pub['FieldName'])
        with meta_col4:
            st.metric("Region", selected_pub['region_group'])

        st.divider()

        # Abstract
        if pd.notna(selected_pub.get('Abstract')):
            st.subheader("Abstract")
            st.write(selected_pub['Abstract'])

        # DOI
        if pd.notna(selected_pub.get('DOI')):
            st.subheader("Publication Link")
            doi = selected_pub['DOI']
            st.markdown(f"[https://doi.org/{doi}](https://doi.org/{doi})")

    with col2:
        st.metric("Own-Region Citation %", f"{selected_pub['own_region_cite_share']:.1%}")
        st.metric("Foreign-Region Citation %", f"{selected_pub['foregin_region_cite_share']:.1%}")
        st.metric("Journal", selected_pub.get('Sourcetitle', 'N/A'))

        # Simple pie chart
        fig_pie = go.Figure(data=[go.Pie(
            labels=['Own Region', 'Foreign Regions'],
            values=[selected_pub['own_region_cite_share'], selected_pub['foregin_region_cite_share']],
            hole=0.3
        )])
        st.plotly_chart(fig_pie, width="stretch")

else:
    st.warning("No publications match the selected filters.")

# Footer
st.divider()
st.markdown("""
**About this dashboard:**
- Data source: Publications from top 0.1% normalized citations, filtered for regional focus
- Last updated: July 5, 2026
- Methodology: Citations normalized by field and publication year; only includes publications
  where own-region citation share exceeds 75%
""")
