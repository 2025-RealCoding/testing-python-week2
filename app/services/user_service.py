import cv2
import numpy as np
from datetime import datetime
from app.face.face_embedding import *
from app.face.face_db import *

def register_user(user_id: str, image_bytes: bytes) -> dict:
    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    embedding = extract_embedding(image)
    save_user(user_id, embedding)
    return {'user_id': user_id, 'registered_at': str(datetime.now())}


def authenticate_user(image_bytes: bytes):
   image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    db = load_db()
    embedding_to_check = extract_embedding(image)
    for user_id, data in db.items():
        if verify_embedding(data['embedding'], embedding_to_check):
            return user_id
    return None


def get_user(user_id):
    db = load_db()
    user_data = db.get(user_id)
    if user_data:
        return {'user_id': user_id, 'registered_at': user_data['registered_at']}
    return None


def delete_user(user_id):
    db = load_db()
    if user_id in db:
        del db[user_id]
        save_db(db)
        return True
    return False
