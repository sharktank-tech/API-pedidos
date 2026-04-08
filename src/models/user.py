from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# =====================
# Usuários
# =====================
class User(UserMixin):
    def __init__(
        self,
        id: int,
        username: str,
        email: str,
        password_hash: str = None,
        is_admin: bool = False,
        created_at: str = None,
        updated_at: str = None,
    ):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.is_admin = is_admin
        self.created_at = self._parse_date(created_at)
        self.updated_at = self._parse_date(updated_at)

    # -------- Password --------
    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)

    # -------- Helpers --------
    @staticmethod
    def _parse_date(value):
        if not value:
            return None
        try:
            return datetime.fromisoformat(value.replace("Z", ""))
        except Exception:
            return None