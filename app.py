import streamlit as st # type: ignore



# 타이틀 추가
st.title("여기에 원하는 타이틀을 입력하세요!")

# 다른 컨텐츠 추가 (예: 그래프, 텍스트 등)
st.write("안녕하세요! 이곳에 다양한 내용을 추가할 수 있습니다.")



# 시연 동영상 첨부
video_url = "https://www.example.com/path/to/your/video.mp4"
st.video(video_url)





st.write("저희의 제품을 구독하시려면 이메일을 입력해주세요.")
email = st.text_input("이메일 입력", "example@example.com")
st.write(f"입력한 이메일: {email}")







# 댓글을 저장할 리스트 생성
comments = []

# 댓글 작성 폼
comment_input = st.text_input("댓글 작성", "")

# 댓글 작성 버튼 클릭 시
if st.button("댓글 작성"):
    if comment_input:
        comments.append(comment_input)
        st.success("댓글이 작성되었습니다!")
    else:
        st.warning("댓글을 입력하세요.")

# 저장된 댓글 표시
if comments:
    st.subheader("댓글 목록")
    for idx, comment in enumerate(comments):
        st.write(f"{idx + 1}. {comment}")
else:
    st.info("아직 댓글이 없습니다.")
