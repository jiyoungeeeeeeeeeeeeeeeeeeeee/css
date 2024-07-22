import streamlit as st # type: ignore



# 타이틀 추가
st.title("여기에 원하는 타이틀을 입력하세요!")

# 다른 컨텐츠 추가 (예: 그래프, 텍스트 등)
st.write("안녕하세요! 이곳에 다양한 내용을 추가할 수 있습니다.")





# 탭 생성: 첫 번째 탭의 이름은 "Tab A", 두 번째 탭은 "Tab B"로 표시합니다.
tab1, tab2, tab3 = st.tabs(['Tab A', '소개합니다.','use'])

with tab1:
    # Tab A를 누르면 표시될 내용
    st.write('Hello from Tab A!')
    # 시연 동영상 첨부
    video_url = "https://www.example.com/path/to/your/video.mp4"
    st.video(video_url)



    # 이메일 입력
    st.write("저희의 제품을 구독하시려면 이메일을 입력해주세요.")
    email = st.text_input("이메일 입력", "example@example.com")
    st.write(f"입력한 이메일: {email}")
    import re
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return True
        else:
            return False
        # 사용 예시
    user_email = input("이메일 주소를 입력하세요: ")
    if validate_email(user_email):
        st.write("유효한 이메일 주소입니다.")
    else:
        st.write("유효하지 않은 이메일 주소입니다.")







with tab2:
    # Tab B를 누르면 표시될 내용
    st.write('동화책 창작에 도움을 주는 것에 대하여')
    long_markdown = """
    # 제목
    # 여기에 긴 장문의 텍스트를 마크다운으로 작성하세요.
    # - 리스트 항목 1
    # - 리스트 항목 2
    # """
    # 
    st.markdown(long_markdown)





with tab3:
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
    




# 좋아요 버튼 클릭 여부를 세션 상태로 관리
if 'like_button' not in st.session_state:
    st.session_state.like_button = False

def handle_like():
    st.session_state.like_button = not st.session_state.like_button
    if st.session_state.like_button:
        st.write('❤️ 이 글을 좋아합니다!')
    else:
        st.write('❤️ 좋아요 취소')

# 좋아요 버튼 생성
if st.button('좋아요'):
    handle_like()