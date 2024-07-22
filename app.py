import streamlit as st # type: ignore



# 타이틀 추가
st.title("여기에 원하는 타이틀을 입력하세요!")

# 다른 컨텐츠 추가 (예: 그래프, 텍스트 등)
st.write("안녕하세요! 이곳에 다양한 내용을 추가할 수 있습니다.")




video_url = "https://www.example.com/path/to/your/video.mp4"
st.video(video_url)
st.write("저희의 제품을 소개합니다.")




st.write("저희의 제품을 구독하시려면 이메일을 입력해주세요.")
email = st.text_input("이메일 입력", "example@example.com")
st.write(f"입력한 이메일: {email}")