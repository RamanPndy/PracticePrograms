from functools import wraps
from flask import request, jsonify
from systemdesign.authentication_framework.services import AuthService

class AuthMiddleware:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service

    def token_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split(" ")[1]
            if not token:
                return jsonify({'message': 'Token is missing!'}), 403

            try:
                data = self.auth_service.verify_token(token)
                current_user = self.auth_service.users.get(data['username'])
            except Exception as e:
                return jsonify({'message': str(e)}), 403

            return f(current_user, *args, **kwargs)
        return decorated
