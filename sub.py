import streamlit as st
import random
import time

st.title("🪜 사다리타기로 메뉴 선택하기")

# 1. 사용자 메뉴 입력
menu_input = st.text_input("🍱 메뉴들을 쉼표(,)로 입력해 주세요", placeholder="예: 김밥, 라면, 돈까스, 초밥")
menus = [m.strip() for m in menu_input.split(",") if m.strip()]

if len(menus) < 2:
    st.warning("메뉴를 2개 이상 입력해 주세요.")
else:
    if st.button("🪜 사다리 타기 시작!"):
        st.write("사다리를 타고 내려갑니다...")
        with st.spinner("사다리를 타는 중..."):
            time.sleep(2)  # 사다리 타는 듯한 지연 효과

        # 사다리 시뮬레이션 결과 출력
        picked = random.choice(menus)
        st.success(f"🎉 오늘의 당첨 메뉴는 **{picked}** 입니다!")

        # 시각적으로 보여주기 (텍스트 사다리 스타일 흉내)
        st.write("---")
        st.markdown("### 🎲 사다리 결과")
        for menu in menus:
            if menu == picked:
                st.markdown(f"➡️ **{menu}** 🎯")
            else:
                st.markdown(f"➖ {menu}")
