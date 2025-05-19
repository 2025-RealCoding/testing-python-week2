from pydantic import BaseModel


class UserResponse(BaseModel):
    """회원 응답 모델"""

    user_id: str
    registered_at: str
