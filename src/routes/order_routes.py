from fastapi import APIRouter

order_router = APIRouter()

@order_router.get("/order")
def order():
    return {"Order": "Order",
            "Order ID": "34",
            "Order Date": "2020-07-24",
            "Order Price": "100",
            "Order Quantity": "1",
            "Order Status": "Order Completed",
            "Order Time": "2020-07-24T00:00:00Z",
            } # Subistituir por busca real no banco de dados

@order_router.get("/order{id}")
def order():
        return {"Order": "Order",} # Subistituir por busca real no banco de dados
@order_router.post("/order")
def order():
        return {"Order": "",
                "Order ID": "",
                "Order Date": "",
                "Order Price": "",
                "Order Quantity": "",
                "Order Status": "",
                "Order Time": "",
        }

@order_router.put("/order")
def order():
        return {"Order": "",
                "Order ID": "",
                "Order Date": "",
                "Order Price": "",
                "Order Quantity": "",
                "Order Status": "",
                "Order Time": "",
                }