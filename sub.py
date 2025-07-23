import streamlit as st
import random
import plotly.graph_objects as go

st.title("🎯 메뉴 선택 게임")

st.write("2개 이상의 메뉴를 직접 입력하고, 게임 방식으로 하나를 선택해보세요!")

# 메뉴 입력 (쉼표로 구분)
menu_input = st.text_input("🍱 메뉴들을 쉼표로 구분해 입력하세요 (예: 김밥, 라면, 돈까스)", "")

# 선택 방식
game_mode = st.radio("🎲 선택 방식", ["룰렛", "사다리타기"])

# 입력된 메뉴 리스트
menus = [m.strip() for m in menu_input.split(",") if m.strip()]

if len(menus) < 2:
    st.warning("메뉴를 2개 이상 입력해주세요.")
else:
    if st.button("▶️ 시작하기"):
        picked = random.choice(menus)

        if game_mode == "룰렛":
            # 룰렛 시각화
            fig = go.Figure(data=[go.Pie(
                labels=menus,
                values=[1]*len(menus),
                hole=0.3,
                textinfo="label",
                pull=[0.1 if m == picked else 0 for m in menus]
            )])
            fig.update_layout(title="🍀 룰렛 결과!", showlegend=False)
            st.plotly_chart(fig)
            st.success(f"🎉 오늘의 당첨 메뉴는: **{picked}** 입니다!")
        
        elif game_mode == "사다리타기":
            # 간단한 텍스트 기반 사다리 결과 출력
            st.write("사다리 타기 결과는...")
            st.markdown("🔻 **" + picked + "** 당첨!")
            st.balloons()
