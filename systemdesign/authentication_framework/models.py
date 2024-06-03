import uuid
import hashlib
from datetime import datetime

class User:
    def __init__(self, username: str, email: str, password: str):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password_hash = self.hash_password(password)
        self.created_at = datetime.now()

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        return self.password_hash == self.hash_password(password)
