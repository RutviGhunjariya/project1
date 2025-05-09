import streamlit as st
from main import main
import os

st.title("🎬 AI Powered Text-to-Video Generator")

user_input = st.text_area("Enter your story text here", height=300)

if st.button("Generate Video"):
    with st.spinner("Creating your amazing video..."):
        video_path = main(user_input)
        if os.path.exists(video_path):
            st.success("Video generated successfully!")
            st.video(video_path)
        else:
            st.error("Something went wrong during video creation.")
