import streamlit as st # type: ignore

video_url = "https://www.example.com/path/to/your/video.mp4"
st.video(video_url)



email = st.text_input("이메일 입력", "example@example.com")
st.write(f"입력한 이메일: {email}")