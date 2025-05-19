import pytest

from app.face.face_embedding import *

def test_extract_embedding():
    # Given
    image_path = 'images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg'

    # When
    embedding = extract_embedding(image_path)

    # Then
    assert embedding is not None
    assert len(embedding) > 0

def test_no_fact_exception():
    # Given
    image_path = 'tests/images/no_face.jpg'

    # When
    # Then
    with pytest.raises(ValueError):
        extract_embedding(image_path)

def test_verify_embedding():
    # Given
    image_path1 = 'images/Aaron_Peirsol/Aaron_Peirsol_0001.jpg'
    image_path2 = 'images/Aaron_Peirsol/Aaron_Peirsol_0002.jpg'
    image_path3 = 'images/Olivia_Newton-John/Olivia_Newton-John_0001.jpg'

    embedding1 = extract_embedding(image_path1)
    embedding2 = extract_embedding(image_path2)
    embedding3 = extract_embedding(image_path3)

    # When
    # Then
    assert verify_embedding(embedding1, embedding2)
    assert not verify_embedding(embedding1, embedding3)