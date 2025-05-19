import pytest

from app.face.face_embedding import extract_embedding, verify_embedding


def test_extract_embedding():
    # Given: 얼굴이 명확하게 보이는 이미지 파일이 주어짐
    image_path = "images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg"

    # When: 얼굴 임베딩 추출 기능을 실행
    embedding = extract_embedding(image_path)

    # Then: 임베딩이 추출된다. 임베딩 길이는 0보다 큼
    assert embedding is not None
    assert len(embedding) > 0


def test_no_face_exception():
    # Given: 얼굴이 명확하게 보이지 않는 이미지 파일이 주어짐
    image_path = "tests/images/no_face.jpg"

    # When: 얼굴 임베딩 추출 기능을 실행
    # Then: 예외가 발생함
    with pytest.raises(ValueError):
        extract_embedding(image_path)


def test_verify_embedding():
    # Given: 얼굴 임베딩이 주어짐
    image_path1 = "images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg"
    image_path2 = "images/Aaron_Peirsol/Aaron_Peirsol_0002.jpg"
    image_path3 = "images/Olivia_Newton-John/Olivia_Newton-John_0001.jpg"

    embedding1 = extract_embedding(image_path1)
    embedding2 = extract_embedding(image_path2)
    embedding3 = extract_embedding(image_path3)

    # When: 얼굴 임베딩 검증 기능을 실행
    # Then: 동일 사람인 경우 검증 결과가 True, 다른 사람인 경우 검증 결과가 False
    assert verify_embedding(embedding1, embedding2)
    assert not verify_embedding(embedding1, embedding3)
