import streamlit as st
from pytubefix import YouTube

st.set_page_config(page_title="YouTube Video Downloader", page_icon="🎥")

st.title("🎥 YouTube Video Downloader – Day 27")
st.write("Enter a valid YouTube video URL to download.")

video_url = st.text_input("🔗 Enter YouTube Video URL:")

if st.button("Download Video"):
    if not video_url.strip():
        st.error("Please enter a YouTube URL!")
    else:
        try:
            yt = YouTube(video_url)

            st.success(f"📌 Title: {yt.title}")
            st.write(f"👤 Channel: {yt.author}")

            stream = yt.streams.get_highest_resolution()

            with st.spinner("Downloading..."):
                stream.download()

            st.success("✅ Video downloaded successfully!")

        except Exception as e:
            st.error("❌ YouTube blocked this request or video is unavailable.")
            st.code(str(e))
