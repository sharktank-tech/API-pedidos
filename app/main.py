from fastapi import FastAPI
from app.routers import users

app = FastAPI(
    title="Pedidos",
    description="API de gestão de pedidos",
    version="1.0.0"
)

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API funcionando"}