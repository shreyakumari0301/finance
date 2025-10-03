import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timedelta
import feedparser

# Fintech keywords
FINTECH_KEYWORDS = [
    'fintech', 'financial technology', 'digital banking', 'mobile payment',
    'cryptocurrency', 'crypto', 'blockchain', 'digital wallet', 'neobank',
    'robo advisor', 'insurtech', 'regtech', 'paytech', 'wealthtech',
    'lending', 'peer to peer', 'p2p', 'crowdfunding', 'digital currency',
    'defi', 'decentralized finance', 'open banking', 'api banking',
    'embedded finance', 'buy now pay later', 'bnpl', 'fintech startup'
]

# Classification keywords
GLOBAL_KEYWORDS = ['global', 'international', 'worldwide', 'cross-border']
NATIONAL_KEYWORDS = ['national', 'domestic', 'local', 'country', 'government']
FUNDING_KEYWORDS = ['funding', 'investment', 'venture capital', 'vc', 'series', 'ipo', 'acquisition']

# News sources
NEWS_SOURCES = {
    'Fintech News': 'https://www.fintechnews.org/feed/',
    'Finextra': 'https://www.finextra.com/rss/feeds.aspx',
    'TechCrunch': 'https://techcrunch.com/category/fintech/feed/'
}

def get_articles(days_back=14):
    """Get articles from RSS feeds"""
    all_articles = []
    cutoff_date = datetime.now() - timedelta(days=days_back)
    
    for source_name, rss_url in NEWS_SOURCES.items():
        try:
            feed = feedparser.parse(rss_url)
            for entry in feed.entries[:10]:
                try:
                    pub_date = datetime(*entry.published_parsed[:6]) if hasattr(entry, 'published_parsed') else datetime.now()
                    if pub_date >= cutoff_date:
                        all_articles.append({
                            'title': entry.title,
                            'description': entry.get('summary', ''),
                            'url': entry.link,
                            'publishedAt': pub_date.strftime('%Y-%m-%d'),
                            'source': source_name
                        })
                except:
                    continue
        except:
            continue
    
    return all_articles

def is_fintech_related(title, description):
    """Check if article is fintech-related"""
    text = f"{title} {description}".lower()
    return any(keyword.lower() in text for keyword in FINTECH_KEYWORDS)

def classify_news(title, description):
    """Classify news"""
    text = f"{title} {description}".lower()
    
    if any(keyword in text for keyword in FUNDING_KEYWORDS):
        return 'Funding'
    elif any(keyword in text for keyword in GLOBAL_KEYWORDS):
        return 'Global'
    else:
        return 'National'

def main():
    st.set_page_config(page_title="Fintech News", page_icon="📰", layout="wide")
    
    # CSS
    st.markdown("""
    <style>
    .stApp { background-color: #f8fafc !important; }
    .main-header { font-size: 2.5rem; color: #2563eb; text-align: center; margin-bottom: 2rem; font-weight: bold; }
    .section-header { display: flex; justify-content: space-between; align-items: center; margin: 2rem 0 1rem 0; padding: 1rem 0; border-bottom: 2px solid #e5e7eb; }
    .section-header h2 { color: #1f2937; font-size: 1.8rem; font-weight: 700; margin: 0; }
    .article-count { background: linear-gradient(135deg, #2563eb, #3b82f6); color: white; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.9rem; font-weight: 600; }
    .article-card { background-color: white; padding: 1rem; border-radius: 8px; border: 1px solid #e5e7eb; margin: 0.75rem 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .article-card:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.15); }
    .article-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; }
    .source-badge { background: #6b7280; color: white; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.7rem; font-weight: 500; }
    .time-badge { background-color: #f3f4f6; color: #6b7280; padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.7rem; }
    .article-title { color: #1f2937; font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem; line-height: 1.3; }
    .article-description { color: #6b7280; font-size: 0.85rem; line-height: 1.4; margin-bottom: 0.75rem; }
    .article-footer { display: flex; justify-content: space-between; align-items: center; }
    .classification-badge { padding: 0.2rem 0.6rem; border-radius: 12px; font-size: 0.7rem; font-weight: 600; color: white; }
    .funding { background: #10b981; }
    .global { background: #2563eb; }
    .national { background: #f59e0b; }
    .read-more-link { color: #2563eb; text-decoration: none; font-size: 0.8rem; font-weight: 600; }
    .read-more-link:hover { color: #1e40af; text-decoration: underline; }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">📰 Fintech News Aggregator</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar
    st.sidebar.header("📊 Configuration")
    days_back = st.sidebar.slider("Days to look back", 1, 30, 14)
    
    st.sidebar.markdown("### 🔍 Filter Options")
    show_funding = st.sidebar.checkbox("Show Funding News", value=True)
    show_global = st.sidebar.checkbox("Show Global News", value=True)
    show_national = st.sidebar.checkbox("Show National News", value=True)
    
    # Main content
    if st.button("🔄 Refresh News", type="primary"):
        with st.spinner("Fetching news..."):
            articles = get_articles(days_back)
            
            if articles:
                # Filter fintech articles
                fintech_articles = []
                for article in articles:
                    if is_fintech_related(article['title'], article['description']):
                        classification = classify_news(article['title'], article['description'])
                        article['classification'] = classification
                        fintech_articles.append(article)
                
                if fintech_articles:
                    df = pd.DataFrame(fintech_articles)
                    st.success(f"✅ Found {len(df)} fintech articles!")
                    
                    # Metrics
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Total", len(df))
                    with col2:
                        funding_count = len(df[df['classification'] == 'Funding'])
                        st.metric("Funding", funding_count)
                    with col3:
                        global_count = len(df[df['classification'] == 'Global'])
                        st.metric("Global", global_count)
                    with col4:
                        national_count = len(df[df['classification'] == 'National'])
                        st.metric("National", national_count)
                    
                    st.markdown("---")
                    
                    # Filter based on sidebar
                    filtered_df = df.copy()
                    classifications_to_show = []
                    if show_funding:
                        classifications_to_show.append('Funding')
                    if show_global:
                        classifications_to_show.append('Global')
                    if show_national:
                        classifications_to_show.append('National')
                    
                    if classifications_to_show:
                        filtered_df = filtered_df[filtered_df['classification'].isin(classifications_to_show)]
                    
                    # Create sections
                    funding_articles = filtered_df[filtered_df['classification'] == 'Funding'] if show_funding else pd.DataFrame()
                    global_articles = filtered_df[filtered_df['classification'] == 'Global'] if show_global else pd.DataFrame()
                    national_articles = filtered_df[filtered_df['classification'] == 'National'] if show_national else pd.DataFrame()
                    
                    # Display sections
                    if not global_articles.empty:
                        st.markdown("---")
                        st.markdown(f"""
                        <div class="section-header">
                            <h2>🌍 Global</h2>
                            <span class="article-count">{len(global_articles)} articles</span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        cols = st.columns(2)
                        for idx, (_, row) in enumerate(global_articles.iterrows()):
                            col_idx = idx % 2
                            with cols[col_idx]:
                                st.markdown(f"""
                                <div class="article-card">
                                    <div class="article-header">
                                        <span class="source-badge">{row['source']}</span>
                                        <span class="time-badge">{row['publishedAt']}</span>
                                    </div>
                                    <h5 class="article-title">{row['title']}</h5>
                                    <p class="article-description">{row['description'][:150]}{'...' if len(row['description']) > 150 else ''}</p>
                                    <div class="article-footer">
                                        <span class="classification-badge global">{row['classification']}</span>
                                        <a href="{row['url']}" target="_blank" class="read-more-link">Read more →</a>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                    
                    if not national_articles.empty:
                        st.markdown("---")
                        st.markdown(f"""
                        <div class="section-header">
                            <h2>🏛️ National</h2>
                            <span class="article-count">{len(national_articles)} articles</span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        cols = st.columns(2)
                        for idx, (_, row) in enumerate(national_articles.iterrows()):
                            col_idx = idx % 2
                            with cols[col_idx]:
                                st.markdown(f"""
                                <div class="article-card">
                                    <div class="article-header">
                                        <span class="source-badge">{row['source']}</span>
                                        <span class="time-badge">{row['publishedAt']}</span>
                                    </div>
                                    <h5 class="article-title">{row['title']}</h5>
                                    <p class="article-description">{row['description'][:150]}{'...' if len(row['description']) > 150 else ''}</p>
                                    <div class="article-footer">
                                        <span class="classification-badge national">{row['classification']}</span>
                                        <a href="{row['url']}" target="_blank" class="read-more-link">Read more →</a>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                    
                    if not funding_articles.empty:
                        st.markdown("---")
                        st.markdown(f"""
                        <div class="section-header">
                            <h2>💰 Funding</h2>
                            <span class="article-count">{len(funding_articles)} articles</span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        cols = st.columns(2)
                        for idx, (_, row) in enumerate(funding_articles.iterrows()):
                            col_idx = idx % 2
                            with cols[col_idx]:
                                st.markdown(f"""
                                <div class="article-card">
                                    <div class="article-header">
                                        <span class="source-badge">{row['source']}</span>
                                        <span class="time-badge">{row['publishedAt']}</span>
                                    </div>
                                    <h5 class="article-title">{row['title']}</h5>
                                    <p class="article-description">{row['description'][:150]}{'...' if len(row['description']) > 150 else ''}</p>
                                    <div class="article-footer">
                                        <span class="classification-badge funding">{row['classification']}</span>
                                        <a href="{row['url']}" target="_blank" class="read-more-link">Read more →</a>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                    
                    # Download
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download CSV",
                        data=csv,
                        file_name=f"fintech_news_{datetime.now().strftime('%Y%m%d')}.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No fintech-related articles found.")
            else:
                st.error("Failed to fetch articles.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6c757d; margin-top: 2rem; padding: 2rem; background-color: white; border-radius: 12px; border: 1px solid #e5e7eb;'>
        <p><strong>📰 Fintech News Aggregator</strong> | Built with Streamlit</p>
        <p><small>Scrapes news from multiple fintech sources</small></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
