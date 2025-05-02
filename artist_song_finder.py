import streamlit as st
import pandas as pd

# Set page configuration (sabse pehla Streamlit command hona chahiye)
st.set_page_config(page_title="Artist-wise Song Finder", page_icon="🎵")

# Load dataset
df = pd.read_csv('spotify_data.csv')

# App Title
st.title("Artist-wise Song Finder 🎵")

# Artist input
artist_input = st.text_input("Enter Artist Name:")

# Case insensitive match
if artist_input:
    artist_songs = df[df['artist_name'].str.lower() == artist_input.lower()]

    if not artist_songs.empty:
        st.success(f"✅ Found {len(artist_songs)} songs by **{artist_input}**")
        st.dataframe(
            artist_songs[['track_name', 'genre', 'popularity', 'year']].drop_duplicates().reset_index(drop=True),
            use_container_width=True
        )
    else:
        st.error("❌ No songs found for this artist. Try different spelling or check spacing.")

# Footer
st.markdown("---")
st.caption("🎵 Built with ❤️ using Streamlit")