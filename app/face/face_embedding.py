import numpy as np
from deepface import DeepFace
from typing import Union

def extract_embedding(img_path: Union[str, np.ndarray]) -> list:
    embedding = DeepFace.represent(img_path)[0]['embedding']
    return embedding


def verify_embedding(embedding1: list, embedding2: list) -> bool:
    is_same_person = DeepFace.verify(embedding1, embedding2)['verified']
    return is_same_person
