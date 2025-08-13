# util.py
"""
Simple utilities for tournament data processing.
No complex dependencies - just basic filtering and text processing.
"""

from datetime import date
from dateutil.parser import parse as parse_date
import logging

logger = logging.getLogger(__name__)

def filter_upcoming(tournaments):
    """
    Filter tournaments to show only upcoming ones (start_date >= today).
    Returns list of upcoming tournaments.
    """
    if not tournaments:
        return []
    
    today = date.today()
    upcoming = []
    
    for tournament in tournaments:
        start_date_str = tournament.get("start_date", "")
        
        if not start_date_str:
            continue
            
        try:
            start_date = parse_date(start_date_str).date()
            if start_date >= today:
                upcoming.append(tournament)
        except Exception as e:
            logger.warning(f"Could not parse date '{start_date_str}': {e}")
            continue
    
    return upcoming

def clean_and_enrich(tournaments):
    """
    Clean tournament data and remove duplicates.
    Simple version without complex summarization.
    """
    if not tournaments:
        return []
    
    seen = set()
    cleaned = []
    
    for tournament in tournaments:
        # Create unique key for duplicate detection
        name = tournament.get("name", "").strip().lower()
        sport = tournament.get("sport", "").strip().lower()
        start_date = tournament.get("start_date", "")
        
        key = (name, sport, start_date)
        
        if key in seen or not name:  # Skip duplicates and entries without names
            continue
            
        seen.add(key)
        
        # Ensure all required fields exist with clean values
        cleaned_tournament = {
            "name": tournament.get("name", "").strip(),
            "sport": tournament.get("sport", "").strip(),
            "level": tournament.get("level", "Unknown").strip(),
            "start_date": tournament.get("start_date", ""),
            "end_date": tournament.get("end_date", tournament.get("start_date", "")),
            "tournament_url": tournament.get("tournament_url", ""),
            "streaming_link": tournament.get("streaming_link", ""),
            "image_url": tournament.get("image_url", ""),
            "summary": clean_summary(tournament.get("summary", ""))
        }
        
        # Generate basic summary if missing
        if not cleaned_tournament["summary"]:
            cleaned_tournament["summary"] = f"{cleaned_tournament['sport']} tournament at {cleaned_tournament['level']} level."
        
        cleaned.append(cleaned_tournament)
    
    logger.info(f"Cleaned {len(cleaned)} tournaments from {len(tournaments)} raw entries")
    return cleaned

def clean_summary(summary):
    """
    Clean and limit summary text length.
    """
    if not summary:
        return ""
    
    # Remove extra whitespace
    cleaned = " ".join(summary.strip().split())
    
    # Limit to reasonable length (150 characters)
    if len(cleaned) > 150:
        cleaned = cleaned[:147] + "..."
    
    return cleaned

def get_sports_list(tournaments):
    """
    Get unique list of sports from tournaments.
    """
    sports = set()
    for tournament in tournaments:
        sport = tournament.get("sport", "").strip()
        if sport:
            sports.add(sport)
    return sorted(list(sports))

def get_levels_list(tournaments):
    """
    Get unique list of levels from tournaments.
    """
    levels = set()
    for tournament in tournaments:
        level = tournament.get("level", "").strip()
        if level:
            levels.add(level)
    return sorted(list(levels))

def format_date_range(start_date, end_date):
    """
    Format date range for display.
    """
    if not start_date:
        return "Date TBD"
    
    if not end_date or start_date == end_date:
        return start_date
    
    return f"{start_date} to {end_date}"
