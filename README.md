# GenAI Sports Tournament Calendar

A GenAI-powered solution that generates an up-to-date calendar of sports tournaments using TheSportsDB API with AI-generated summaries. Built as part of a GenAI intern assignment to demonstrate real-world data collection and AI integration.

## 🎯 Assignment Overview

This project fulfills the requirement to build a GenAI-powered solution for sports tournament calendar generation, covering multiple sports and competition levels with real-world upcoming tournament data.

## 🚀 Live Demo

**[View Live Application](https://your-app-url.streamlit.app)** *(Replace with your actual deployed URL)*

## ✨ Features

- **Real-time Data**: Fetches live upcoming tournaments from TheSportsDB API
- **AI-Powered Summaries**: Uses transformers (DistilBART) to generate tournament summaries (max 50 words)
- **Multi-Sport Coverage**: Cricket, Football, Basketball, Baseball, and more
- **Multiple Competition Levels**: International, National, State, Corporate, School, etc.
- **Export Functionality**: Download tournament data as CSV
- **Dual View Modes**: Table view for data analysis, Card view for visual browsing
- **Real-time Filtering**: Filter by sport type and competition level

## 🏆 Supported Sports & Levels

### Sports Covered
- Soccer, American Football, Basketball, Baseball
- Badminton, Running, Gym, Cycling, Swimming
- Kabaddi, Yoga, Chess, Table Tennis

### Competition Levels
- International, National, Zonal/Regional, State
- District, Corporate, College/University
- Club/Academy, School

## 📊 Output Format

The application provides tournament data in the required format:
- **Tournament Name**
- **Level** (Competition level)
- **Start Date**
- **End Date** 
- **Tournament Official URL**
- **Streaming Partners/Links**
- **Tournament Image**
- **Summary** (AI-generated, max 50 words)

## 🛠️ Technical Approach

### System Design
1. **Data Collection**: TheSportsDB API for real-world tournament data
2. **AI Processing**: HuggingFace Transformers for summary generation
3. **Data Filtering**: Python utilities for upcoming events only
4. **UI Framework**: Streamlit for rapid prototyping and deployment
5. **Storage**: In-memory processing with CSV export capability

### Data Accuracy & Quality
- **Real-time API**: Ensures up-to-date tournament information
- **Data Validation**: Filters out incomplete or past tournaments
- **AI Fallback**: Custom text generation when API descriptions are missing
- **Error Handling**: Graceful handling of API failures and network issues

### Scalability Considerations
- **Lazy Loading**: AI model loads only when needed
- **Efficient API Calls**: Targeted league-specific requests
- **Caching Strategy**: Streamlit built-in caching for performance
- **Modular Design**: Easy to extend with new sports/leagues

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Internet connection (for API and AI model)

### Installation & Setup
```bash
# Clone the repository
git clone https://github.com/NikitaSingh13/SPORTS-CALENDER.git
cd SPORTS-CALENDER

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 📁 Project Structure

```
SPORTS-CALENDER/
├── app.py              # Streamlit web interface
├── data.py             # API integration & AI processing
├── util.py             # Data filtering utilities
├── requirements.txt    # Python dependencies
└── README.md          # This documentation
```

## 🔧 Core Components

### 1. Data Collection (`data.py`)
- **API Integration**: TheSportsDB free API for tournament data
- **AI Processing**: DistilBART model for summary generation
- **League Coverage**: Premier League, NBA, MLB, NFL
- **Data Enrichment**: Custom text building for comprehensive summaries

### 2. User Interface (`app.py`)
- **Interactive Filters**: Sport and level selection
- **Dual Views**: Table (analytical) and Card (visual) modes
- **Export Feature**: CSV download functionality
- **Responsive Design**: Works on desktop and mobile

### 3. Data Processing (`util.py`)
- **Date Filtering**: Shows only upcoming tournaments
- **Data Validation**: Ensures complete tournament information
- **Clean Architecture**: Modular and maintainable code

## 📈 Sample Output

```json
{
  "name": "Premier League Match",
  "sport": "Soccer",
  "level": "International",
  "start_date": "2025-08-20",
  "end_date": "2025-08-20",
  "tournament_url": "https://premierleague.com",
  "streaming_link": "",
  "image_url": "https://example.com/image.jpg",
  "summary": "Exciting Premier League match featuring top teams..."
}
```

## 🎯 Bonus Features Implemented

✅ **Web UI**: Full Streamlit application with interactive features  
✅ **Export API**: CSV download functionality  
✅ **Real-time Data**: Live API integration  
✅ **AI Integration**: Automated summary generation  
✅ **Responsive Design**: Works across devices  

## ⚠️ Limitations & Future Improvements

### Current Limitations
- **API Dependency**: Limited to TheSportsDB free tier leagues
- **Local Tournaments**: Currently focuses on major international leagues
- **Storage**: In-memory processing (no persistent database)
- **Real-time Updates**: Manual refresh required

### Planned Improvements
1. **Database Integration**: SQLite/MySQL for persistent storage
2. **REST API**: Dedicated API endpoints (`GET /tournaments`)
3. **Local Tournament Data**: Web scraping for regional events
4. **Auto-refresh**: Scheduled data updates
5. **Enhanced Filtering**: More granular search options

## 🔗 API Endpoint (Future)

```bash
# Planned API structure
GET /tournaments?sport=soccer&level=international
GET /tournaments/export?format=csv
POST /tournaments/refresh
```

## 🛡️ Error Handling

- **Network Issues**: Graceful API failure handling
- **Missing Data**: AI-generated fallback summaries
- **Invalid Dates**: Automatic filtering and validation
- **Model Loading**: Progressive enhancement for AI features

## 📦 Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and export
- **requests**: API communication
- **transformers**: AI text summarization
- **torch**: Machine learning backend
- **python-dateutil**: Date processing

## 🤝 Assignment Compliance

This project fully addresses the GenAI intern assignment requirements:
- ✅ GenAI-powered tournament calendar
- ✅ Multiple sports coverage
- ✅ All competition levels
- ✅ Required output format
- ✅ Real-world upcoming data
- ✅ AI-generated summaries
- ✅ Web UI implementation
- ✅ Export functionality

---

**Built with ❤️ using Streamlit, TheSportsDB API, and HuggingFace Transformers**

*GenAI Intern Assignment | Noida/Hybrid | 3-month Internship Path to Full Time*
