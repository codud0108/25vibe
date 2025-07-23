import streamlit as st
import random

# 앱 제목 표시
st.title("오늘 뭐 먹지?")

# 점심 메뉴 리스트 (원하는 메뉴를 추가 및 수정할 수 있습니다)
menus = [
    "김치찌개", "된장찌개", "비빔밥", "불고기",
    "햄버거", "피자", "김밥", "볶음밥", "라면", "초밥"
]

# 사이드바에 기본 설정 메뉴
st.sidebar.header("설정")
# 메뉴를 제외할 항목 선택 (여러 메뉴 중 선택하여 추천 제외 가능)
exclude_menu = st.sidebar.multiselect("제외할 메뉴를 선택하세요:", menus)

# 제외된 메뉴를 리스트에서 제거
available_menus = [menu for menu in menus if menu not in exclude_menu]

# 메인 페이지에 설명
st.write("### 점심 메뉴 추천 받기")
st.write("아래 버튼을 눌러 오늘 먹을 메뉴를 추천받으세요.")

# 추천 버튼
if st.button("오늘의 메뉴 추천"):
    if available_menus:  # 사용 가능한 메뉴가 있는 경우
        recommendation = random.choice(available_menus)
        st.success(f"오늘의 추천 메뉴는 **{recommendation}** 입니다!")
    else:
        st.error("선택 가능한 메뉴가 없습니다. 제외 설정을 해제해 주세요.")

# 사용자의 선호 메뉴 저장 기능 (간단한 예제)
st.write("### 선호 메뉴 저장")
favorite_menu = st.text_input("평소 좋아하는 메뉴를 입력해 주세요:")

if st.button("저장"):
    if favorite_menu:
        st.info(f"'{favorite_menu}' 를 좋아하는 메뉴로 저장했어요!")
    else:
        st.warning("메뉴를 입력해 주세요.")
