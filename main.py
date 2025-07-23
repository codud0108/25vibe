import streamlit as st
import random

# --- 카테고리별 메뉴 정의 ---
menu_dict = {
    "한식": [
        "김치찌개", "된장찌개", "부대찌개", "비빔밥", "불고기", "제육볶음", "갈비탕", "삼계탕", "순두부찌개", "떡볶이",
        "칼국수", "냉면", "쫄면", "비빔국수", "수육국밥", "콩나물국밥", "육회비빔밥", "족발", "보쌈", "치킨"
    ],
    "중식": [
        "짜장면", "짬뽕", "탕수육", "마라탕", "마라샹궈", "꿔바로우", "양장피", "유산슬", "깐풍기", "볶음밥"
    ],
    "일식": [
        "초밥", "돈까스", "라멘", "우동", "규동", "가츠동", "오야꼬동", "연어덮밥", "사케동", "나베"
    ],
    "양식": [
        "파스타", "피자", "햄버거", "스테이크", "리조또", "샌드위치", "치즈볼", "그라탱", "수프", "감바스"
    ],
    "기타": [
        "쌀국수", "팟타이", "반미", "나시고랭", "미고랭", "샤브샤브", "김밥", "라면", "컵밥", "핫도그",
        "샐러드", "오므라이스", "두부스테이크", "떡만두국", "아보카도샐러드"
    ]
}

# --- 앱 UI ---
st.title("🍽️ 오늘 뭐 먹지?")
st.write("여러 음식 카테고리를 선택해서 점심 메뉴를 추천받으세요!")

# --- 카테고리 복수 선택 ---
selected_categories = st.multiselect("🍱 카테고리를 선택하세요 (복수 선택 가능)", list(menu_dict.keys()))

# --- 메뉴 구성 ---
if selected_categories:
    # 선택된 카테고리 메뉴 합치기
    combined_menu = []
    for cat in selected_categories:
        combined_menu.extend(menu_dict[cat])

    # --- 제외할 메뉴 선택 ---
    exclude_menu = st.multiselect("❌ 제외할 메뉴를 선택하세요", combined_menu)
    available_menus = [menu for menu in combined_menu if menu not in exclude_menu]

    # --- 추천 버튼 ---
    if st.button("🎲 메뉴 추천 받기"):
        if not available_menus:
            st.warning("추천할 수 있는 메뉴가 없습니다. 제외 항목을 줄여주세요.")
        else:
            picked = random.choice(available_menus)
            st.success(f"오늘의 추천 메뉴는 **{picked}** 입니다! 😋")
else:
    st.info("한 개 이상의 카테고리를 선택해주세요.")
