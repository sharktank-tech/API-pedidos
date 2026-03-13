from fastapi import APIRouter
from app.schemas.user_schema import User
from app.services.user_service import get_users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def list_users():
    return get_users()

@router.post("/")
def create_user(user: User):
    return {"user": user}