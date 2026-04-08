from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


# =====================
class Order(UserMixin):
    def __init__(
        self,
        id: int,
        name: str,
        created_at: str = None,
        status: str = None,
        price: float = None,
        user_id: int = None,
    ):
        self.id = id
        self.name = name
        self.created_at = self._parse_date(created_at)
        self.status = status
        self.price = price
        self.user_id = user_id

    # -------- Password --------
    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)
