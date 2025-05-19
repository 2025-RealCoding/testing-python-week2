from app.face.face_db import load_db, save_user, save_db

db = load_db()
save_db(db)

load_db()
