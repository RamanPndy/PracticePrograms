import jwt
from typing import Dict
from datetime import datetime, timedelta
from systemdesign.authentication_framework.models import User

class AuthService:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.users = {}  # Simulate user storage with an in-memory dictionary

    def register_user(self, username: str, email: str, password: str) -> User:
        if username in self.users:
            raise ValueError("Username already exists")
        user = User(username, email, password)
        self.users[username] = user
        return user

    def login_user(self, username: str, password: str) -> str:
        user = self.users.get(username)
        if not user or not user.check_password(password):
            raise ValueError("Invalid username or password")
        token = self.generate_token(user)
        return token

    def generate_token(self, user: User) -> str:
        payload = {
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def verify_token(self, token: str) -> Dict:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")
