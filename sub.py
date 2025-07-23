import streamlit as st
import random

st.title("🎯 직접 입력한 메뉴 중 오늘의 선택은?")

# 1. 사용자 입력 (쉼표로 구분)
menu_input = st.text_input("🍱 메뉴들을 쉼표(,)로 구분해서 입력해 주세요", placeholder="예: 김밥, 라면, 돈까스")

# 2. 입력된 메뉴 리스트 만들기
menus = [m.strip() for m in menu_input.split(",") if m.strip()]

# 3. 추천 버튼
if st.button("🎲 메뉴 추천받기"):
    if len(menus) < 2:
        st.warning("메뉴를 2개 이상 입력해 주세요.")
    else:
        picked = random.choice(menus)
        st.success(f"오늘은 **{picked}** 어떠세요? 😋")
