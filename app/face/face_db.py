import json, os
from datetime import datetime

DB_PATH = "face_db.json"


def save_user(user_id, embedding):
    db = load_db()
    db[user_id] = {'embedding': embedding, 'registered_at': str(datetime.now())}
    with open(DB_PATH, 'w') as f:
        json.dump(db, f)


def load_db():
    if not os.path.exists(DB_PATH): return {}
    with open(DB_PATH, 'r') as f: return json.load(f)


def save_db(db):
    with open(DB_PATH, 'w') as f: json.dump(db, f)
