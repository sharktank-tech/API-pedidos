from fastapi import APIRouter

users_router = APIRouter()

@users_router.get("/")
async def root():
    return {"message": "A API está no ar!"}

@users_router.get("/user")
def user():
    return {"name": "Fulano",
            "email": "fulano123@email.com",
            }