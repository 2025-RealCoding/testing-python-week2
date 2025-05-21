from app.services.user_service import *

def test_register_user():
    # Given
    image_path = 'images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg'
    user_id = 'aaron_peirsol'

    # When:
    with open(image_path, 'rb') as f:
        image_data = f.read()
        result = register_user(user_id, image_data)

    # Then
    assert result['user_id'] == 'aaron_peirsol'
    assert result['registered_at'] is not None



def test_authenticate_registered_user(setup_user_db):
    # Given
    image_path = "images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg"
    # When
    with open(image_path, 'rb') as f:
        image_data = f.read()
        user_id = authenticate_user(image_data)
    # Then
    assert user_id == 'aaron_peirsol'

def test_authenticate_unregistered_user(setup_user_db):
    # Given
    image_path = 'images/Natasha_McElhone/Natasha_McElhone_0001.jpg'
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # When
    user_id = authenticate_user(image_data)

    # Then
    assert user_id is None

def test_get_registered_user(setup_user_db):
    # Given
    user_id = 'aaron_peirsol'

    # When
    user_info = get_user(user_id)

    # Then
    assert user_info['user_id'] == user_id
    assert 'registered_at' in user_info

def test_delete_registered_user(setup_user_db):
    # Given
    user_id = 'aaron_peirsol'

    # When
    result = delete_user(user_id)

    # Then
    assert result is True

    user_id = get_user(user_id)
    assert user_id is None

def test_non_authenticate_user(setup_user_db):
    # Given: 등록되지 않은 회원
    user_id = 'non_existent_user'

    # When
    user = get_user(user_id) # 등록되지 않은 사용자를

    # Then
    assert user is None # 사용자가 존재하지 않음
