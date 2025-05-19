from app.services.user_service import (
  authenticate_user,
  register_user,
  get_user,
  delete_user,
)

def test_register_user():
  image_path = "images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg"
  user_id = "aaron_peirsol"

  with open(image_path, "rb") as f:
    image_data = f.read()
    result = register_user(user_id, image_data)

  assert result["user_id"] == "aaron_peirsol"
  assert result["registered_at"] is not None

def test_authenticate_registered_user(setup_user_db):
  image_path = "images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg"

  with open(image_path, "rb") as f:
    image_data = f.read()
    user_id = authenticate_user(image_data)
  
  assert user_id == "aaron_peirsol"

def test_authenticate_unregistered_user(setup_user_db):
  image_path = "images/Natasha_McElhone/Natasha_McElhone_0001.jpg"
  with open(image_path, "rb") as f:
    image_data = f.read()

  user_id = authenticate_user(image_data)

  assert user_id is None

def test_get_registered_user(setup_user_db):
  user_id = "aaron_peirsol"

  user_info = get_user(user_id)

  assert user_info["user_id"] == user_id
  assert "registered_at" in user_info

def test_delete_registered_user(setup_user_db):
  user_id = "aaron_peirsol"

  result = delete_user(user_id)

  assert result is True

  user_info = get_user(user_id)
  assert user_info is None

def test_get_unregistered_user(setup_user_db):
  # Given: 등록되지 않은 사용자 ID
  user_id = "aaa"

  # When: 사용자 정보 조회 서비스를 호출
  user_info = get_user(user_id)

  # Then: 사용자 정보 조회 서비스가 None을 반환해야함
  assert user_info == None
