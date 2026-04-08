from fastapi import FastAPI
from src.routes.user_routes import users_router
from src.routes.order_routes import order_router

app = FastAPI()

#app.include_router(order_routes)
app.include_router(users_router)
app.include_router(order_router)