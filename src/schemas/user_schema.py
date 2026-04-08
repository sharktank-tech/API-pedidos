from pydantic import BaseModel

class UserCreate(BaseModel):
    user_id: int
    username: str
    password: str
    email: str
