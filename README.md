# Sports Tournament Calendar

A web application that displays upcoming sports tournaments from TheSportsDB API with AI-generated summaries.

## Features

- Fetches live tournament data from TheSportsDB API
- AI-powered event summaries using transformers
- Filter by sport and competition level
- Table and card view options
- Export tournaments to CSV
- Shows only upcoming events

## Quick Start

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the App
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Supported Sports

- Soccer (Premier League, La Liga)
- Basketball (NBA)
- Baseball (MLB)
- American Football (NFL)

## Project Structure

```
├── app.py              # Streamlit web interface
├── data.py             # API data fetching and AI summaries
├── util.py             # Data filtering utilities
└── requirements.txt    # Dependencies
```

## How It Works

1. **app.py** - Creates the web interface with filters and display options
2. **data.py** - Fetches tournament data from TheSportsDB API and generates AI summaries
3. **util.py** - Filters data to show only upcoming events with valid information

## Dependencies

- **streamlit** - Web framework
- **pandas** - Data handling
- **requests** - API calls
- **transformers** - AI text summarization
- **torch** - ML backend
- **python-dateutil** - Date parsing

## Usage

1. Select a sport from the dropdown
2. Choose competition level
3. Switch between table and card views
4. Download filtered results as CSV

Built with Streamlit and TheSportsDB API
