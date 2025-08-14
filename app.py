import streamlit as st
import pandas as pd
from data import fetch_tournaments
from util import clean_data, filter_upcoming
import io

st.set_page_config(page_title="Sports Tournaments Calendar", layout="wide")
st.title("Sports Tournaments Calendar")

ALL_SPORTS = [
    "Soccer", "American Football","Basketball","Baseball", "Badminton", "Running", "Gym", "Cycling", "Swimming",
    "Kabaddi", "Yoga", "Chess", "Table Tennis"
]

ALL_LEVELS = [
    "International","Corporate", "School", "College/University", "Club/Academy", "District",
    "State", "Zonal/Regional", "National"
]

with st.spinner("Fetching tournaments..."):
    tournaments = fetch_tournaments()

tournaments = filter_upcoming(tournaments)
tournaments = clean_data(tournaments)

sports = ["All"] + ALL_SPORTS
levels = ["All"] + ALL_LEVELS

selected_sport = st.selectbox("Select Sport", sports)
selected_level = st.selectbox("Select Level", levels)

filtered = tournaments
if selected_sport != "All":
    filtered = [t for t in filtered if t["sport"].lower() == selected_sport.lower()]
if selected_level != "All":
    filtered = [t for t in filtered if t["level"].lower() == selected_level.lower()]

top_cols = st.columns([3, 1])
with top_cols[0]:
    view_mode = st.radio("Select View Mode", ["Card View","Table View"], horizontal=True)
with top_cols[1]:
    if filtered:
        df_export = pd.DataFrame(filtered)
        csv_buffer = io.StringIO()
        df_export.to_csv(csv_buffer, index=False)
        st.download_button(
            label="Download CSV",
            data=csv_buffer.getvalue(),
            file_name="upcoming_tournaments.csv",
            mime="text/csv",
            use_container_width=True
        )

if filtered:
    df = pd.DataFrame(filtered)

    if view_mode == "Table View":
        st.dataframe(df[[
            "name", "sport", "level", "start_date", "end_date",
            "tournament_url", "streaming_link", "image_url", "summary"
        ]])

    elif view_mode == "Card View":
        for _, row in df.iterrows():
            with st.container():
                cols = st.columns([1, 3])
                with cols[0]:
                    if row["image_url"]:
                        st.image(row["image_url"], width=350)
                    else:
                        st.write("No image")
                with cols[1]:
                    st.subheader(row["name"])
                    st.write(f"**Sport:** {row['sport']}")
                    st.write(f"**Level:** {row['level']}")
                    st.write(f"**Start:** {row['start_date']} | **End:** {row['end_date']}")
                    st.write(f"**Summary:** {row['summary']}")
                    if row["tournament_url"]:
                        st.markdown(f"[Official Link]({row['tournament_url']})")
else:
    st.warning("No upcoming tournaments.")
