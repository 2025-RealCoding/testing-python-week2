from fastapi import FastAPI

from app.api import users

app = FastAPI()

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "얼굴 인식 기반 회원 관리 API"}
