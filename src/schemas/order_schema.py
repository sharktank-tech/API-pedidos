from pydantic import BaseModel

class OrderSchema(BaseModel):
    order_id: int
    user_id: int
    order_name: str
    order_status: str
    order_date: str
    order_price: float