import streamlit as st
import random

st.set_page_config(page_title="신채호 역사 퀴즈", layout="centered")

st.title("🧠 신채호 역사 퀴즈")
st.markdown("신채호 선생님의 생애와 업적을 퀴즈로 풀어보세요!")

# 퀴즈 데이터
quiz_data = [
    {
        "question": "신채호는 ‘역사는 아(我)와 비아(非我)의 투쟁이다’라고 말했다.",
        "options": ["O", "X"],
        "answer": "O",
        "explanation": "신채호는 민족주의 사학을 주장하며 역사는 주체와 타자의 투쟁이라 정의했습니다."
    },
    {
        "question": "신채호는 대한민국 임시정부 초대 대통령이다.",
        "options": ["O", "X"],
        "answer": "X",
        "explanation": "초대 대통령은 이승만이며, 신채호는 임시정부에 참여하지 않았습니다."
    },
    {
        "question": "신채호는 『조선상고사』라는 책을 집필하였다.",
        "options": ["O", "X"],
        "answer": "O",
        "explanation": "『조선상고사』는 신채호가 쓴 역사서로, 민족 중심의 역사관을 강조합니다."
    },
    {
        "question": "신채호는 일제 강점기 일본의 귀화를 선택했다.",
        "options": ["O", "X"],
        "answer": "X",
        "explanation": "그는 끝까지 저항하며 일본에 협력하지 않았습니다."
    }
]

random.shuffle(quiz_data)

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0

# 퀴즈 진행
if st.session_state.quiz_index < len(quiz_data):
    q = quiz_data[st.session_state.quiz_index]
    st.subheader(f"문제 {st.session_state.quiz_index + 1}:")
    st.write(q["question"])
    user_answer = st.radio("정답을 선택하세요:", q["options"], key=st.session_state.quiz_index)

    if st.button("제출"):
        if user_answer == q["answer"]:
            st.success("✅ 정답입니다!")
            st.session_state.score += 1
        else:
            st.error("❌ 오답입니다.")
        st.info(f"📘 해설: {q['explanation']}")
        st.session_state.quiz_index += 1
        st.experimental_rerun()

else:
    st.success("🎉 퀴즈 완료!")
    st.markdown(f"총 점수: **{st.session_state.score} / {len(quiz_data)}**")
    if st.button("다시 시작하기"):
        st.session_state.quiz_index = 0
        st.session_state.score = 0
        st.experimental_rerun()
