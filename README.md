# API-pedidos

## API de gestão de pedidos 

### Funcionalidades:
- API REST para pedidos
- cadastro de clientes
- status do pedido (recebido, preparando, enviado)
- autenticação JWT
- integração com WhatsApp API para notificar cliente
- webhook para integração com outros sistemas

### Endpoints principais da API
### Usuários
- POST /users
- GET /users
- GET /users/{id}


### Pedidos:
- POST /orders
- GET /orders
- GET /orders/{id}
- PATCH /orders/{id}/status

### Status:

- received
- preparing
- ready
- delivered
- cancelled

### Tecnologias:
- Python + FastAPI
- PostgreSQL
- Redis
- Docker


