import streamlit as st
import random
import plotly.graph_objects as go

st.title("🎡 룰렛으로 점심 메뉴 선택!")

# 메뉴 입력
menu_input = st.text_input("🍱 메뉴들을 쉼표(,)로 입력하세요", placeholder="예: 김밥, 라면, 돈까스, 초밥")

# 입력 메뉴 리스트 처리
menus = [m.strip() for m in menu_input.split(",") if m.strip()]

# 룰렛 실행
if st.button("🎯 룰렛 돌리기"):
    if len(menus) < 2:
        st.warning("메뉴를 2개 이상 입력해 주세요.")
    else:
        # 랜덤 메뉴 선택
        picked = random.choice(menus)

        # Plotly 룰렛 생성
        fig = go.Figure(
            data=[go.Pie(
                labels=menus,
                values=[1]*len(menus),
                hole=0.3,
                textinfo="label+percent",
                pull=[0.1 if m == picked else 0 for m in menus]
            )]
        )
        fig.update_layout(
            title="🍀 룰렛 결과!",
            showlegend=False
        )

        st.plotly_chart(fig)
        st.success(f"🎉 오늘의 추천 메뉴는 **{picked}** 입니다!")
