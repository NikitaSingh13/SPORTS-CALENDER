import re
import requests
from datetime import datetime
from transformers import pipeline

BASE_URL = "https://www.thesportsdb.com/api/v1/json/3/"

SPORT_LEAGUES = {
    "Soccer": [4328, 4335],
    "Basketball": [4387],
    "Baseball": [4424],
    "American Football": [4391],
}

_SUMMARIZER = None

def _get_summarizer():
    global _SUMMARIZER
    if _SUMMARIZER is None:
        _SUMMARIZER = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    return _SUMMARIZER

def _trim_to_words(text: str, max_words: int = 50) -> str:
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words])

def _build_event_text(event: dict, sport: str) -> str:
    name = event.get("strEvent") or f"{event.get('strHomeTeam','?')} vs {event.get('strAwayTeam','?')}"
    league = event.get("strLeague") or ""
    season = event.get("strSeason") or ""
    date = event.get("dateEvent") or event.get("strTimestamp") or ""
    time = event.get("strTime") or ""
    venue = event.get("strVenue") or ""
    city = event.get("strCity") or ""
    country = event.get("strCountry") or ""
    rnd = event.get("intRound") or ""
    stage = event.get("strStage") or ""

    parts = [
        f"{name} is an upcoming {sport} event",
        f"in the {league} {season}".strip() if (league or season) else "",
        f"scheduled on {date}" + (f" at {time} UTC" if time else ""),
        f"at {venue}" if venue else "",
        f"in {city}" if city else "",
        f"{country}" if (country and not city) else "",
        f"Round {rnd}" if rnd else "",
        f"Stage: {stage}" if stage else "",
    ]
    text = ". ".join([p for p in parts if p]).strip(". ")

    teams = [t for t in [event.get("strHomeTeam"), event.get("strAwayTeam")] if t]
    if teams:
        text += f". Teams: {', '.join(teams)}."
    return text

def generate_summary_from_event(event: dict, sport: str) -> str:
    base_text = (event.get("strDescriptionEN") or "").strip()
    if len(base_text.split()) < 25:
        base_text = _build_event_text(event, sport)

    base_text = re.sub(r"\s+", " ", base_text).strip()
    if not base_text:
        return "No summary available"

    if len(base_text.split()) <= 50:
        return base_text

    try:
        summarizer = _get_summarizer()
        out = summarizer(base_text, max_length=80, min_length=25, do_sample=False)
        summary = out[0]["summary_text"].strip()
        return _trim_to_words(summary, 50)
    except Exception as e:
        print("Summarization failed:", e)
        return _trim_to_words(base_text, 50)

def fetch_tournaments():
    tournaments = []

    for sport, leagues in SPORT_LEAGUES.items():
        for league_id in leagues:
            url = f"{BASE_URL}eventsnextleague.php?id={league_id}"
            try:
                resp = requests.get(url, timeout=30)
                resp.raise_for_status()
                data = resp.json()

                for event in data.get("events", []):
                    start_date = event.get("dateEvent")
                    if not start_date:
                        continue

                    try:
                        start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
                    except Exception:
                        continue

                    if start_dt < datetime.today().date():
                        continue

                    summary = generate_summary_from_event(event, sport)

                    tournaments.append({
                        "name": event.get("strEvent") or f"{event.get('strHomeTeam','?')} vs {event.get('strAwayTeam','?')}",
                        "sport": sport,
                        "level": "International",
                        "start_date": start_date,
                        "end_date": start_date,
                        "tournament_url": event.get("strWebsite") or event.get("strOfficial") or "",
                        "streaming_link": "",
                        "image_url": event.get("strThumb") or "",
                        "summary": summary
                    })

            except Exception as e:
                print(f"Error fetching league {league_id} for {sport}:", e)

    return tournaments

if __name__ == "__main__":
    t_list = fetch_tournaments()
    print(f"Fetched {len(t_list)} tournaments")
    for t in t_list[:5]:
        print(t["name"], "→", t["summary"])
