def test_register_user_api(client):
    # Given: 사용자의 ID와 얼굴 이미지가 주어짐
    # Given: API 테스트 클라이언트가 fixture로 제공됨
    image_path = "images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg"
    user_id = "aaron_peirsol"

    # When: 사용자 등록 API (POST /users/register)를 호출
    with open(image_path, "rb") as img_file:
        response = client.post(
            "/users/register",
            data={"user_id": user_id},
            files={"image": ("user1.jpg", img_file, "image/jpeg")},
        )

    # Then: 사용자 등록 기능이 성공(200)
    # Then: 응답 내용은 등록된 사용자 ID 및 등록 시각이 포함
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert data["registered_at"] is not None


def test_authenticate_user_api(client, setup_user_db):
    # Given: 등록된 사용자의 얼굴 이미지가 주어짐
    image_path = "images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg"

    # When: 사용자 인증 API (POST /users/authenticate)를 호출
    with open(image_path, "rb") as img_file:
        response = client.post(
            "/users/authenticate",
            files={"image": ("user1.jpg", img_file, "image/jpeg")},
        )

    # Then: 사용자 인증 기능이 성공(200)
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "aaron_peirsol"


def test_get_registered_user_api(client, setup_user_db):
    # Given: 등록된 사용자 ID
    user_id = "aaron_peirsol"

    # When: 회원 조회 API 호출
    response = client.get(f"/users/{user_id}")

    # Then: 성공적으로 사용자 정보를 반환
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == user_id
    assert "registered_at" in data


def test_delete_registered_user_api(client, setup_user_db):
    # Given: 등록된 사용자 ID
    user_id = "aaron_peirsol"

    # When: 회원 삭제 API 호출
    response = client.delete(f"/users/{user_id}")

    # Then: 삭제 성공 확인
    assert response.status_code == 200

    # 추가 확인: 삭제된 사용자 조회 시 404 확인
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 404
