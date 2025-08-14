from datetime import datetime

def clean_data(tournaments):
    cleaned = []
    for t in tournaments:
        if not t["name"] or not t["start_date"]:
            continue
        cleaned.append(t)
    return cleaned

def filter_upcoming(tournaments):
    today = datetime.today().date()
    return [
        t for t in tournaments
        if datetime.fromisoformat(t["start_date"]).date() >= today
    ]
