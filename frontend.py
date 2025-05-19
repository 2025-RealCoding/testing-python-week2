import requests
import streamlit as st

API_URL = "http://localhost:8000"

st.set_page_config(page_title="얼굴 인식 회원 관리 시스템")

st.title("얼굴 인식 회원 관리 시스템 🚀")

menu = st.sidebar.selectbox(
    "기능 선택", ["회원 등록", "회원 인증", "회원 조회", "회원 삭제"]
)

if menu == "회원 등록":
    st.subheader("📝 회원 등록")

    user_id = st.text_input("사용자 ID")
    image = st.file_uploader("얼굴 이미지 업로드", type=["jpg", "jpeg", "png"])

    if st.button("등록하기"):
        if user_id and image:
            files = {"image": (image.name, image.getvalue(), image.type)}
            data = {"user_id": user_id}

            res = requests.post(f"{API_URL}/users/register", data=data, files=files)

            if res.status_code == 200:
                st.success(f"등록 성공: {res.json()}")
            else:
                st.error(f"등록 실패: {res.json().get('detail')}")
        else:
            st.warning("ID와 이미지를 모두 입력해주세요.")

elif menu == "회원 인증":
    st.subheader("🔑 회원 인증")

    image = st.file_uploader(
        "인증할 얼굴 이미지 업로드", type=["jpg", "jpeg", "png"], key="auth"
    )

    if st.button("인증하기"):
        if image:
            files = {"image": (image.name, image.getvalue(), image.type)}

            res = requests.post(f"{API_URL}/users/authenticate", files=files)

            if res.status_code == 200:
                st.success(f"인증 성공! 사용자 ID: {res.json()['user_id']}")
            else:
                st.error(f"인증 실패: {res.json().get('detail')}")
        else:
            st.warning("이미지를 업로드해주세요.")

elif menu == "회원 조회":
    st.subheader("🔍 회원 조회")

    user_id = st.text_input("조회할 사용자 ID")

    if st.button("조회하기"):
        if user_id:
            res = requests.get(f"{API_URL}/users/{user_id}")

            if res.status_code == 200:
                user_info = res.json()
                st.json(user_info)
            else:
                st.error(f"조회 실패: {res.json().get('detail')}")
        else:
            st.warning("사용자 ID를 입력해주세요.")

elif menu == "회원 삭제":
    st.subheader("🗑️ 회원 삭제")

    user_id = st.text_input("삭제할 사용자 ID")

    if st.button("삭제하기"):
        if user_id:
            res = requests.delete(f"{API_URL}/users/{user_id}")

            if res.status_code == 200:
                st.success("성공적으로 삭제되었습니다.")
            else:
                st.error(f"삭제 실패: {res.json().get('detail')}")
        else:
            st.warning("사용자 ID를 입력해주세요.")
