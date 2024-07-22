import streamlit as st # type: ignore



# 타이틀 추가
st.title("여기에 원하는 타이틀을 입력하세요!")

# 다른 컨텐츠 추가 (예: 그래프, 텍스트 등)
st.write("안녕하세요! 이곳에 다양한 내용을 추가할 수 있습니다.")



# 카테고리 생성
category = st.selectbox('카테고리 선택', ['공포', '로맨틱', '미스테리', '고전문학'])

# 선택한 카테고리에 따라 내용 표시
if category == '공포':
    st.write('오싹한게 좋아!')
elif category == '로맨틱':
    st.write('꾸준히 사랑받는 것엔 이유가 있다.')
elif category == '미스테리':
    st.write('나는 인류가 풀지 못한 난제들이 궁금해.')
else:
    st.write('그 당시 사람들의 지혜를 빌려보고 싶어.')





# 탭 생성: 첫 번째 탭의 이름은 "Tab A", 두 번째 탭은 "Tab B"로 표시합니다.
tab1, tab2 = st.tabs(['Tab A', 'Tab B'])

with tab1:
    # Tab A를 누르면 표시될 내용
    st.write('Hello from Tab A!')

with tab2:
    # Tab B를 누르면 표시될 내용
    st.write('Hi from Tab B!')






# 시연 동영상 첨부
video_url = "https://www.example.com/path/to/your/video.mp4"
st.video(video_url)



# 이메일 입력
st.write("저희의 제품을 구독하시려면 이메일을 입력해주세요.")
email = st.text_input("이메일 입력", "example@example.com")
st.write(f"입력한 이메일: {email}")







# 게시글의 좋아요 수 (임의로 초기값 설정)
likes_count = 10


# 좋아요 버튼
if st.button(st.markdown('<button class="heart-button">❤️ Like</button>', unsafe_allow_html=True)):
    likes_count += 1
    st.write(f"게시글이 좋아요! 현재 좋아요 수: {likes_count}")
else:
    st.write(f"게시글 좋아요 수: {likes_count}")

