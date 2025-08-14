# Sports Tournament Calendar

A simple and clean web application to discover upcoming sports tournaments using TheSportsDB API. Built with Streamlit and designed to be easy to understand and extend.

## Features

- **Live API Data**: Fetches real-time tournament data from TheSportsDB API
- **Multiple Sports Coverage**: Soccer, Basketball, Baseball, American Football
- **Smart Filtering**: Filter by sport type and competition level
- **Upcoming Events**: Automatically shows only future tournaments
- **AI-Powered Summaries**: Uses AI to generate event summaries
- **Dual View Modes**: Choose between table view and card view with images
- **Responsive Design**: Works great on desktop and mobile devices

## Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Internet connection (required for API data)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/NikitaSingh13/SPORTS-CALENDER.git
   cd SPORTS-CALENDER
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL shown in your terminal

## Project Structure

```
SPORTS-CALENDER/
│
├── app.py              
├── data.py             
├── util.py             
├── requirements.txt    
├── README.md           
└── __pycache__/        
```

## Data Source

### TheSportsDB API
- **Free sports data API** for major sports leagues
- **Real-time data** for upcoming matches and tournaments
- **Multiple sports** including Soccer, Basketball, Baseball, etc.

### Supported Sports & Leagues
- **Soccer**: Premier League, La Liga
- **Basketball**: NBA
- **Baseball**: MLB
- **American Football**: NFL

## How It Works

### Data Flow
1. **app.py** → Main Streamlit interface with filters and dual view modes
2. **data.py** → Fetches tournament data from TheSportsDB API and generates AI summaries
3. **util.py** → Cleans data and filters for upcoming events only
4. **Display** → Shows filtered tournaments in table or card format with images

### Key Functions

#### `data.py`
- `fetch_tournaments()`: Main function to fetch all tournament data from API
- `_get_summarizer()`: Lazy-loads AI summarization model for event descriptions
- `_build_event_text()`: Creates descriptive text from event data for AI processing

#### `util.py`
- `filter_upcoming()`: Filters tournaments to show only future events (today or later)
- `clean_data()`: Removes tournaments with missing names or dates

#### `app.py`
- Streamlit interface with sport and level filters
- Table view with searchable dataframe
- Card view with images and detailed event information
- Automatic data fetching with loading spinner

## Customization

### Adding New Sports/Leagues
1. Find league IDs from TheSportsDB API documentation
2. Add them to `SPORT_LEAGUES` dictionary in `data.py`:
   ```python
   SPORT_LEAGUES = {
       "Your Sport": [league_id_1, league_id_2],
       "Soccer": [4328, 4335],
   }
   ```

### Modifying AI Summaries
1. Update the summarization model in `data.py`:
   ```python
   _SUMMARIZER = pipeline("summarization", model="your-preferred-model")
   ```
2. Adjust the `_trim_to_words()` function for different summary lengths

### Customizing the UI
- Modify the view modes in `app.py`
- Adjust the column layout and card design
- Add new filter options by extending the selectbox options

## AI Features

### Automatic Event Summaries
The application uses AI to generate concise summaries for each tournament:
- **Model**: DistilBART CNN (sshleifer/distilbart-cnn-12-6) via HuggingFace Transformers
- **Purpose**: Creates readable summaries from raw API event data
- **Optimization**: Lazy loading ensures the AI model loads only when needed
- **Fallback**: If AI processing fails, displays basic event information

### How AI Summaries Work
1. Raw event data is collected from TheSportsDB API
2. Event details are formatted into descriptive text
3. AI model processes the text to create concise summaries
4. Summaries are trimmed to approximately 50 words for consistency

## Troubleshooting

### Common Issues

1. **"No tournaments found"**
   - Check your internet connection
   - The TheSportsDB API might be temporarily unavailable
   - Try refreshing the page to reload data

2. **Installation errors**
   - Ensure Python 3.7+ is installed: `python --version`
   - Try: `pip install --upgrade pip` then retry installation
   - For Windows users: Use `pip3` instead of `pip` if needed

3. **App won't start**
   - Make sure all dependencies are installed: `pip list`
   - Try: `streamlit --version` to verify Streamlit is installed
   - Check if port 8501 is already in use

4. **AI model loading issues**
   - First run may take longer as the AI model downloads
   - Ensure stable internet connection for model download
   - Check disk space (models can be several hundred MB)

5. **API connection issues**
   - Verify internet connectivity
   - Check firewall settings
   - TheSportsDB API might be temporarily down

### Performance Tips
- **First Run**: Initial startup may be slow due to AI model loading
- **Memory**: AI models require additional RAM (recommend 4GB+ available)
- **Internet**: Stable connection needed for both API calls and model downloads

### Getting Help
- Check the terminal output for detailed error messages
- Ensure all required files are in the project directory
- Verify internet connectivity for API calls

## Development

### Code Structure
- **API-First Design**: Fetches real-time data from TheSportsDB
- **AI Integration**: Uses HuggingFace Transformers for event summaries
- **Error Handling**: Graceful handling of API failures and missing data
- **Lazy Loading**: AI model is loaded only when needed for better performance
- **Date Filtering**: Automatic filtering to show only upcoming events

### Dependencies
The project uses several key libraries:
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and display
- **Requests**: HTTP requests to TheSportsDB API
- **Transformers**: AI model for text summarization
- **Torch**: PyTorch backend for AI models
- **python-dateutil**: Date parsing utilities

### Adding Features
1. **New View Modes**: Extend the radio button options in `app.py`
2. **Additional Filters**: Add more selectbox filters for different data fields
3. **New League IDs**: Add more sports leagues in the `SPORT_LEAGUES` dictionary
4. **Enhanced AI**: Experiment with different summarization models
5. **Styling**: Customize the Streamlit interface with CSS

### Development Setup
1. Fork the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Make your changes and test locally
6. Submit a pull request

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs or issues
- Suggest new features
- Submit pull requests for improvements
- Add support for more sports leagues
- Improve the AI summarization

## Contact

- **Repository**: [SPORTS-CALENDER](https://github.com/NikitaSingh13/SPORTS-CALENDER)
- **Issues**: Report bugs or request features via GitHub Issues

---

**Built with using Streamlit, TheSportsDB API, and AI-powered summaries**
