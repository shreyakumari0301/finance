# Fintech News Aggregator

A Streamlit-based application that fetches fintech news from Google News API, filters relevant content, and classifies articles into Global, National, and Funding categories.

## Features

- 📰 Fetches news from the past 14 days (configurable)
- 🔍 Filters for fintech-related content using keyword matching
- 📊 Classifies news into three categories:
  - **Global**: International fintech developments
  - **National**: Domestic fintech news and regulations
  - **Funding**: Investment rounds, acquisitions, and funding news
- 🎨 Light-themed Streamlit interface
- 📥 Export functionality to CSV
- ⚙️ Configurable filters and date ranges

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   streamlit run fintech_news_aggregator.py
   ```

3. **Access the app:**
   Open your browser to `http://localhost:8501`

## Configuration

- **API Key**: Already configured with your GNews API key
- **Date Range**: Adjustable from 1-30 days (default: 14 days)
- **Article Limit**: Configurable from 10-200 articles (default: 100)
- **Filters**: Toggle visibility for different news categories

## Usage

1. Click "🔄 Refresh News" to fetch the latest articles
2. Use sidebar filters to show/hide specific categories
3. View articles with their classification and source information
4. Download results as CSV for further analysis

## API Information

- **Provider**: GNews.io
- **Endpoint**: https://gnews.io/api/v4/search
- **Rate Limits**: Check GNews.io documentation for current limits

## Classification Logic

The app uses keyword-based classification:

- **Funding**: Articles containing funding, investment, VC, series rounds, etc.
- **Global**: International, worldwide, cross-border developments
- **National**: Domestic, local, government, regulatory news
- **Default**: Falls back to National if no clear indicators

## Deployment

For production deployment, consider:
- Environment variables for API keys
- Caching mechanisms for API responses
- Scheduled runs (every 14 days as planned)
- Database storage for historical data

## License

This project is for educational and personal use.
