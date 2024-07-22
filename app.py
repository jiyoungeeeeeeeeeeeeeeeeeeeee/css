import streamlit as st # type: ignore



# 타이틀 추가
st.title("여기에 원하는 타이틀을 입력하세요!")

# 다른 컨텐츠 추가 (예: 그래프, 텍스트 등)
st.write("안녕하세요! 이곳에 다양한 내용을 추가할 수 있습니다.")



# 카테고리 생성
category = st.selectbox('카테고리 선택', ['기술', '디자인', '마케팅', '기타'])

# 선택한 카테고리에 따라 내용 표시
if category == '기술':
    st.write('기술 카테고리 내용을 여기에 작성하세요.')
elif category == '디자인':
    st.write('디자인 카테고리 내용을 여기에 작성하세요.')
elif category == '마케팅':
    st.write('마케팅 카테고리 내용을 여기에 작성하세요.')
else:
    st.write('기타 카테고리 내용을 여기에 작성하세요.')





# 시연 동영상 첨부
video_url = "https://www.example.com/path/to/your/video.mp4"
st.video(video_url)



st.write("저희의 제품을 구독하시려면 이메일을 입력해주세요.")
email = st.text_input("이메일 입력", "example@example.com")
st.write(f"입력한 이메일: {email}")







