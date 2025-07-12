import streamlit as st
from emotion_detect import detect_emotion_from_webcam
from music_recommend import recommend_music
from config import emotion_to_genre

st.set_page_config(page_title="MoodTunes", layout="centered")
st.title("🎵 MoodTunes - Emotion Based Music Recommender")

if st.button("Detect Mood"):
    emotion = detect_emotion_from_webcam()
    st.success(f"Detected Emotion: {emotion.capitalize()}")

    genre = emotion_to_genre.get(emotion, "pop")
    st.info(f"Recommended Genre: {genre.title()}")

    tracks = recommend_music(genre)
    st.subheader("🎧 Recommended Songs:")
    for i, track in enumerate(tracks, 1):
        st.markdown(f"**{i}. {track['name']}** — {track['artist']}")
        st.markdown(f"[Listen]({track['url']})")

st.markdown("""<hr style="margin-top: 50px;">
<p style='text-align: center; font-size: 14px; color: gray;'>
    Made with ❤️ by <b>Jasim Fazil</b>
</p>""", unsafe_allow_html=True)
