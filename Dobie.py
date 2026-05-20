import streamlit as st
import pandas as pd
from datetime import date
from streamlit_option_menu import option_menu
from PIL import Image, ImageOps

with st.sidebar:
    st.write("##   LIST")
    
    # 예쁜 세로 메뉴판 만들기
    selected = option_menu(
        menu_title=None, # 메뉴판 전체 타이틀 (생략 가능)
        options=["Dobie","gallery"], # 메뉴 목록
        icons=["house","file-image"], # 아이콘 이름 (bootstrap icons 검색해서 매칭 가능)
        menu_icon="cast", 
        default_index=0, # 처음에 기본으로 선택되어 있을 항목 번호
        styles={
            "container": {"": "5px", "background-color": "transparent",  "border": "none"}, 
            "icon": {"color": "black", "font-size": "16px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "background-color": "transparent","--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#FF69B4"},
        }
    )

# 사용자가 선택한 메뉴에 따라 오른쪽 메인 화면 출력
if selected == "Dobie":
    dobie_icon = Image.open("DB_icon.PNG")
    st.image(dobie_icon, width=150)
    st.markdown("""
        <h1 style="font-size: 50px; font-weight: 700; margin-top: -35px; margin-bottom: 0px; padding-top: 20px;">
            <span style="color: #FF69B4;"> 정도비</span> 연구소
        </h1>
    """, unsafe_allow_html=True)
    st.divider()

    birth_date = date(2012, 7, 29)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    c1, c2, c3, c4 = st.columns([1.5,1,1,1], vertical_alignment="center")
    with c1:
        st.markdown("""
            <div style="text-align: center;">
                <p style="color: #666666; font-size: 14px; margin-bottom: 0px;">생일</p>
                <span style="margin: 4px 0px; font-size: 36px; font-weight: 600; display: block;">2012.07.29</span>
                <p style="color: #888888; font-size: 14px; margin-top: 0px;">도비랑 처음만난 날 🎂</p>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div style="text-align: center;">
                <p style="color: #666666; font-size: 14px; margin-bottom: 0px;">나이</p>
                <span style="margin: 4px 0px; font-size: 36px; font-weight: 600; display: block;">만 {age}세</span>
                <p style="color: #888888; font-size: 14px; margin-top: 0px;">아직 애기랍니다</p>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
            <div style="text-align: center;">
                <p style="color: #666666; font-size: 14px; margin-bottom: 0px;">성별</p>
                <span style="margin: 4px 0px; font-size: 36px; font-weight: 600; display: block;">여</span>
                <p style="color: #888888; font-size: 14px; margin-top: 0px;">♀</p>
            </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
            <div style="text-align: center;">
                <p style="color: #666666; font-size: 14px; margin-bottom: 0px;">몸무게</p>
                <span style="margin: 4px 0px; font-size: 36px; font-weight: 600; display: block;">🤫쉿</span>
                <p style="color: #888888; font-size: 14px; margin-top: 0px;">말랑말랑하세요</p>
            </div>
        """, unsafe_allow_html=True)
    st.divider()

    dobie = Image.open("DB.PNG")
    st.image(dobie)



elif selected == "gallery":
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <div style="color: #888888; font-size: 22px; font-weight: 500; margin-bottom: -10px;">
                🤫 비밀스러운
            </div>
            <div style="color: #000000; font-size: 52px; font-weight: 800; letter-spacing: -1px;">
                일상 사진 
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # 💡 여기서부터 들여쓰기 라인을 세로로 똑바르게 청소했습니다!
    col1, col2, col3 = st.columns(3)

    # 파이썬 이미지 라이브러리로 안전하게 열기 (공백 4칸 라인으로 정렬 완료)
    img1 = Image.open("JDB.jpeg")
    img2 = Image.open("JDB2.jpeg")
    img3 = Image.open("JDB3.jpeg")
    
    # 사진 3장의 크기를 가로 400px, 세로 300px로 칼같이 통일
    img1 = ImageOps.fit(img1, (400, 300), Image.Resampling.LANCZOS)
    img2 = ImageOps.fit(img2, (400, 300), Image.Resampling.LANCZOS)
    img3 = ImageOps.fit(img3, (400, 300), Image.Resampling.LANCZOS)

    # 각 컬럼(칸) 안에 사진과 설명 배치
    with col1:
        st.image(img1, use_container_width=True)
        st.caption("2024.11.15")
        st.caption("평소에는 차분하신데, 기분이 안좋으신 날이었나봐요😅")

    with col2:
        st.image(img2, use_container_width=True)
        st.caption("2022.11.08")
        st.caption("화면 가득하게 보면 더 귀여우시답니다❤️")

    with col3:
        st.image(img3, use_container_width=True)
        st.caption("2022.11.08")
        st.caption("최애 인형을 뜨거운 눈빛으로 바라보시는 모습!🔥")

