# Fintech News Aggregator

A Streamlit-based application that fetches fintech news from RSS feeds, filters relevant content, and classifies articles into Global, National, and Funding categories.

## Features

- 📰 Fetches news from RSS feeds (past 14 days, configurable)
- 🔍 Filters for fintech-related content using keyword matching
- 📊 Classifies news into three categories:
  - **Global**: International fintech developments
  - **National**: Domestic fintech news and regulations
  - **Funding**: Investment rounds, acquisitions, and funding news
- 🎨 Modern light-themed Streamlit interface with responsive design
- 📥 Export functionality to CSV
- ⚙️ Configurable filters and date ranges
- 📱 Responsive layout with article cards

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   streamlit run app.py
   ```

3. **Access the app:**
   Open your browser to `http://localhost:8501`

## Configuration

- **Date Range**: Adjustable from 1-30 days (default: 14 days)
- **News Sources**: RSS feeds from Fintech News, Finextra, and TechCrunch
- **Filters**: Toggle visibility for different news categories
- **Article Limit**: Up to 10 articles per source

## Usage

1. Click "🔄 Refresh News" to fetch the latest articles
2. Use sidebar filters to show/hide specific categories
3. View articles with their classification and source information
4. Download results as CSV for further analysis

## News Sources

The app fetches from these RSS feeds:
- **Fintech News**: https://www.fintechnews.org/feed/
- **Finextra**: https://www.finextra.com/rss/feeds.aspx
- **TechCrunch Fintech**: https://techcrunch.com/category/fintech/feed/

## Classification Logic

The app uses keyword-based classification:

- **Funding**: Articles containing funding, investment, VC, series, IPO, acquisition
- **Global**: International, worldwide, cross-border developments
- **National**: Domestic, local, government, regulatory news (default fallback)

## Dependencies

- `streamlit` - Web application framework
- `requests` - HTTP requests
- `pandas` - Data manipulation
- `beautifulsoup4` - HTML parsing
- `feedparser` - RSS feed parsing

## Deployment

For production deployment, consider:
- Environment variables for configuration
- Caching mechanisms for RSS responses
- Scheduled runs for regular updates
- Database storage for historical data
- Error handling for RSS feed failures

## License

This project is for educational and personal use.
