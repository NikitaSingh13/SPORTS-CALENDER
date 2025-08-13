# data.py
"""
Simple data fetching for sports tournaments.
Uses TheSportsDB API and fallback mock data.
"""

import requests
from datetime import datetime, date
from dateutil.parser import parse as parse_date
import logging

# Setup simple logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TheSportsDB API (free tier)
API_KEY = "1"
BASE_URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}"

# Comprehensive mock data for all sports
MOCK_TOURNAMENTS = [
    # Cricket
    {
        "name": "ICC Cricket World Cup 2025",
        "sport": "Cricket", 
        "level": "International",
        "start_date": "2025-10-05",
        "end_date": "2025-11-19",
        "tournament_url": "https://www.icc-cricket.com/world-cup",
        "streaming_link": "https://www.hotstar.com",
        "image_url": "https://via.placeholder.com/400x200.png?text=Cricket+World+Cup",
        "summary": "The biggest cricket tournament featuring teams from around the world."
    },
    {
        "name": "Indian Premier League 2025",
        "sport": "Cricket",
        "level": "Domestic",
        "start_date": "2025-03-20",
        "end_date": "2025-05-15",
        "tournament_url": "https://www.iplt20.com",
        "streaming_link": "https://www.hotstar.com",
        "image_url": "https://via.placeholder.com/400x200.png?text=IPL+2025",
        "summary": "India's premier T20 cricket league with international stars."
    },
    
    # Football
    {
        "name": "FIFA World Cup 2026 Qualifiers",
        "sport": "Football",
        "level": "International", 
        "start_date": "2025-09-01",
        "end_date": "2025-11-30",
        "tournament_url": "https://www.fifa.com",
        "streaming_link": "https://www.fifa.com/live",
        "image_url": "https://via.placeholder.com/400x200.png?text=FIFA+Qualifiers",
        "summary": "Qualifying matches for the 2026 FIFA World Cup."
    },
    {
        "name": "Premier League 2025-26",
        "sport": "Football",
        "level": "Domestic",
        "start_date": "2025-08-16",
        "end_date": "2026-05-24",
        "tournament_url": "https://www.premierleague.com",
        "streaming_link": "https://www.peacocktv.com",
        "image_url": "https://via.placeholder.com/400x200.png?text=Premier+League",
        "summary": "England's top football league with the world's best players."
    },
    
    # Basketball
    {
        "name": "NBA Finals 2025",
        "sport": "Basketball",
        "level": "Professional",
        "start_date": "2025-06-05",
        "end_date": "2025-06-22",
        "tournament_url": "https://www.nba.com",
        "streaming_link": "https://www.nba.com/live",
        "image_url": "https://via.placeholder.com/400x200.png?text=NBA+Finals",
        "summary": "The championship series of the National Basketball Association."
    },
    {
        "name": "FIBA Basketball World Cup 2025",
        "sport": "Basketball",
        "level": "International",
        "start_date": "2025-08-25",
        "end_date": "2025-09-10",
        "tournament_url": "https://www.fiba.basketball",
        "streaming_link": "https://www.fiba.basketball/live",
        "image_url": "https://via.placeholder.com/400x200.png?text=FIBA+World+Cup",
        "summary": "International basketball championship by FIBA."
    },
    
    # Badminton
    {
        "name": "BWF World Championships 2025",
        "sport": "Badminton",
        "level": "International",
        "start_date": "2025-08-25",
        "end_date": "2025-08-31",
        "tournament_url": "https://bwfbadminton.com",
        "streaming_link": "https://www.bwftv.com",
        "image_url": "https://via.placeholder.com/400x200.png?text=BWF+Championships",
        "summary": "The premier global badminton championship."
    },
    {
        "name": "All England Open 2025",
        "sport": "Badminton",
        "level": "International",
        "start_date": "2025-03-12",
        "end_date": "2025-03-16",
        "tournament_url": "https://www.allenglandbadminton.com",
        "streaming_link": "https://www.bwftv.com",
        "image_url": "https://via.placeholder.com/400x200.png?text=All+England+Open",
        "summary": "The world's oldest badminton tournament."
    },
    
    # Tennis
    {
        "name": "Wimbledon 2025",
        "sport": "Tennis",
        "level": "Grand Slam",
        "start_date": "2025-06-30",
        "end_date": "2025-07-13",
        "tournament_url": "https://www.wimbledon.com",
        "streaming_link": "https://www.wimbledon.com/live",
        "image_url": "https://via.placeholder.com/400x200.png?text=Wimbledon+2025",
        "summary": "The most prestigious tennis championship on grass courts."
    },
    
    # Swimming
    {
        "name": "World Aquatics Championships 2025",
        "sport": "Swimming",
        "level": "International",
        "start_date": "2025-07-18",
        "end_date": "2025-08-03",
        "tournament_url": "https://www.worldaquatics.com",
        "streaming_link": "https://www.worldaquatics.com/live",
        "image_url": "https://via.placeholder.com/400x200.png?text=World+Swimming",
        "summary": "Premier international swimming and aquatics championship."
    },
    
    # Running
    {
        "name": "Boston Marathon 2025",
        "sport": "Running",
        "level": "International",
        "start_date": "2025-04-21",
        "end_date": "2025-04-21",
        "tournament_url": "https://www.baa.org",
        "streaming_link": "https://www.baa.org/live",
        "image_url": "https://via.placeholder.com/400x200.png?text=Boston+Marathon",
        "summary": "One of the six World Marathon Majors."
    },
    
    # Chess
    {
        "name": "World Chess Championship 2025",
        "sport": "Chess",
        "level": "International",
        "start_date": "2025-11-01",
        "end_date": "2025-11-30",
        "tournament_url": "https://www.fide.com",
        "streaming_link": "https://www.chess.com/live",
        "image_url": "https://via.placeholder.com/400x200.png?text=Chess+Championship",
        "summary": "The ultimate chess championship to determine the world champion."
    },
    
    # Table Tennis
    {
        "name": "World Table Tennis Championships 2025",
        "sport": "Table Tennis",
        "level": "International",
        "start_date": "2025-09-20",
        "end_date": "2025-09-29",
        "tournament_url": "https://www.ittf.com",
        "streaming_link": "https://www.ittf.com/live",
        "image_url": "https://via.placeholder.com/400x200.png?text=Table+Tennis+World",
        "summary": "The premier table tennis championship event."
    }
]

def fetch_from_sportsdb(sport_name="Soccer"):
    """
    Fetch upcoming events from TheSportsDB API.
    Returns list of tournaments or empty list if failed.
    """
    tournaments = []
    
    try:
        # Get upcoming events for a specific sport
        url = f"{BASE_URL}/eventsseason.php?id=4328&s=2024-2025"  # Premier League example
        
        # For simplicity, just get some general upcoming events
        url = f"{BASE_URL}/eventsnext.php?id=133602"  # Example league ID
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        events = data.get("events", [])
        
        for event in events[:5]:  # Limit to 5 events
            try:
                tournament = {
                    "name": event.get("strEvent", "Unknown Event"),
                    "sport": sport_name,
                    "level": "Professional",
                    "start_date": parse_event_date(event.get("dateEvent")),
                    "end_date": parse_event_date(event.get("dateEvent")),
                    "tournament_url": event.get("strWebsite", ""),
                    "streaming_link": "",
                    "image_url": event.get("strThumb", ""),
                    "summary": clean_text(event.get("strDescriptionEN", ""))
                }
                tournaments.append(tournament)
            except Exception as e:
                logger.warning(f"Error parsing event: {e}")
                continue
                
    except Exception as e:
        logger.error(f"TheSportsDB API failed: {e}")
    
    return tournaments

def parse_event_date(date_str):
    """Parse date string to YYYY-MM-DD format."""
    if not date_str:
        return ""
    
    try:
        parsed_date = parse_date(date_str).date()
        return parsed_date.isoformat()
    except Exception:
        return date_str

def clean_text(text):
    """Clean and truncate text."""
    if not text:
        return ""
    
    # Remove extra whitespace and limit length
    cleaned = " ".join(text.split())
    if len(cleaned) > 200:
        cleaned = cleaned[:200] + "..."
    
    return cleaned

def get_tournaments():
    """
    Main function to get all tournaments.
    Returns a list of tournament dictionaries.
    """
    all_tournaments = []
    
    # Start with mock data (always reliable)
    all_tournaments.extend(MOCK_TOURNAMENTS)
    
    # Try to fetch from TheSportsDB (optional enhancement)
    try:
        api_tournaments = fetch_from_sportsdb("Football")
        if api_tournaments:
            all_tournaments.extend(api_tournaments)
            logger.info(f"Added {len(api_tournaments)} tournaments from API")
    except Exception as e:
        logger.warning(f"API fetch failed, using mock data only: {e}")
    
    # Ensure all tournaments have required fields
    standardized_tournaments = []
    for tournament in all_tournaments:
        standardized = {
            "name": tournament.get("name", "Unknown Tournament"),
            "sport": tournament.get("sport", "Unknown"),
            "level": tournament.get("level", "Unknown"),
            "start_date": tournament.get("start_date", ""),
            "end_date": tournament.get("end_date", ""),
            "tournament_url": tournament.get("tournament_url", ""),
            "streaming_link": tournament.get("streaming_link", ""),
            "image_url": tournament.get("image_url", "https://via.placeholder.com/400x200.png?text=Tournament"),
            "summary": tournament.get("summary", "Tournament information not available.")
        }
        standardized_tournaments.append(standardized)
    
    logger.info(f"Total tournaments loaded: {len(standardized_tournaments)}")
    return standardized_tournaments
