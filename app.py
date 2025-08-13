# app.py
"""
Simple Sports Tournament Calendar App
Displays upcoming sports tournaments with filtering options.
"""

import streamlit as st
import pandas as pd
from data import get_tournaments
from util import filter_upcoming, clean_and_enrich, get_sports_list, get_levels_list, format_date_range

# Page configuration
st.set_page_config(
    page_title="Sports Tournament Calendar",
    page_icon="🏆",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .tournament-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        background-color: #f9f9f9;
    }
    .tournament-title {
        color: #1f77b4;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .tournament-meta {
        color: #666;
        font-size: 14px;
        margin-bottom: 15px;
    }
    .stButton > button {
        background-color: #1f77b4;
        color: white;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.title("🏆 Sports Tournament Calendar")
st.markdown("### Discover upcoming sports tournaments from around the world")

# Load data with error handling
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_tournament_data():
    """Load and process tournament data with caching."""
    try:
        with st.spinner("Loading tournaments..."):
            raw_tournaments = get_tournaments()
            upcoming_tournaments = filter_upcoming(raw_tournaments)
            clean_tournaments = clean_and_enrich(upcoming_tournaments)
            return clean_tournaments
    except Exception as e:
        st.error(f"Error loading tournament data: {e}")
        return []

tournaments = load_tournament_data()

if not tournaments:
    st.warning("No tournament data available. Please check your internet connection.")
    st.stop()

# Sidebar filters
st.sidebar.header("🔍 Filter Tournaments")

# Get unique sports and levels
sports_list = get_sports_list(tournaments)
levels_list = get_levels_list(tournaments)

selected_sport = st.sidebar.selectbox(
    "Select Sport:",
    ["All Sports"] + sports_list,
    help="Filter tournaments by sport type"
)

selected_level = st.sidebar.selectbox(
    "Select Level:",
    ["All Levels"] + levels_list,
    help="Filter tournaments by competition level"
)

# Search functionality
search_term = st.sidebar.text_input(
    "Search tournaments:",
    placeholder="Enter tournament name...",
    help="Search by tournament name"
)

# Apply filters
filtered_tournaments = tournaments.copy()

if selected_sport != "All Sports":
    filtered_tournaments = [t for t in filtered_tournaments if t.get("sport") == selected_sport]

if selected_level != "All Levels":
    filtered_tournaments = [t for t in filtered_tournaments if t.get("level") == selected_level]

if search_term:
    filtered_tournaments = [
        t for t in filtered_tournaments 
        if search_term.lower() in t.get("name", "").lower()
    ]

# Display results summary
st.markdown(f"### 📅 Showing {len(filtered_tournaments)} tournaments")

if len(filtered_tournaments) == 0:
    st.info("No tournaments match your current filters. Try adjusting your search criteria.")
    st.stop()

# Sort tournaments by date
try:
    filtered_tournaments.sort(key=lambda x: x.get("start_date", "9999-12-31"))
except:
    pass  # If sorting fails, display in original order

# Display tournaments in a responsive grid
cols = st.columns(2)

for i, tournament in enumerate(filtered_tournaments):
    col = cols[i % 2]
    
    with col:
        # Tournament card container
        with st.container():
            # Tournament image
            image_url = tournament.get("image_url")
            if image_url and image_url != "https://via.placeholder.com/400x200.png?text=Tournament":
                st.image(image_url, use_container_width=True)
            else:
                st.image(
                    f"https://via.placeholder.com/400x200.png?text={tournament.get('sport', 'Tournament').replace(' ', '+')}",
                    use_container_width=True
                )
            
            # Tournament details
            st.markdown(f"**{tournament.get('name', 'Unknown Tournament')}**")
            
            # Meta information
            sport = tournament.get('sport', 'Unknown')
            level = tournament.get('level', 'Unknown')
            st.markdown(f"🏃 **Sport:** {sport} | 🏆 **Level:** {level}")
            
            # Date information
            start_date = tournament.get('start_date', '')
            end_date = tournament.get('end_date', '')
            date_range = format_date_range(start_date, end_date)
            st.markdown(f"📅 **Dates:** {date_range}")
            
            # Summary
            summary = tournament.get('summary', 'No description available.')
            st.markdown(f"📋 {summary}")
            
            # Links
            col1, col2 = st.columns(2)
            
            with col1:
                if tournament.get('tournament_url'):
                    st.markdown(f"[🌐 Official Site]({tournament['tournament_url']})")
            
            with col2:
                if tournament.get('streaming_link'):
                    st.markdown(f"[📺 Watch Live]({tournament['streaming_link']})")
            
            st.markdown("---")

# Footer
st.markdown("---")
st.markdown("### 📊 Tournament Statistics")

# Create summary statistics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Tournaments", len(filtered_tournaments))

with col2:
    unique_sports = len(set(t.get('sport', '') for t in filtered_tournaments))
    st.metric("Sports Covered", unique_sports)

with col3:
    with_streaming = len([t for t in filtered_tournaments if t.get('streaming_link')])
    st.metric("With Live Streaming", with_streaming)

with col4:
    international_count = len([t for t in filtered_tournaments if 'international' in t.get('level', '').lower()])
    st.metric("International Events", international_count)

# Data table view (optional)
if st.checkbox("📋 Show detailed table view"):
    df_data = []
    for tournament in filtered_tournaments:
        df_data.append({
            "Tournament": tournament.get('name', ''),
            "Sport": tournament.get('sport', ''),
            "Level": tournament.get('level', ''),
            "Start Date": tournament.get('start_date', ''),
            "End Date": tournament.get('end_date', ''),
        })
    
    if df_data:
        df = pd.DataFrame(df_data)
        st.dataframe(df, use_container_width=True)
        st.write("---")

# Also allow CSV download
if tournaments:
    df = pd.DataFrame(filtered_tournaments)
    csv = df.to_csv(index=False)
    st.download_button("Download CSV", data=csv, file_name="tournaments.csv", mime="text/csv")
else:
    st.info("No tournaments available.")
