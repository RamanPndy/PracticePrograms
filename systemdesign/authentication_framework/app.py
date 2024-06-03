'''
Components
User: Represents a user with unique credentials.
AuthService: Manages user registration, login, and token issuance.
TokenService: Manages creation and validation of tokens.
Middleware: Handles token validation for different services.
'''
from flask import Flask, request, jsonify
from systemdesign.authentication_framework.middleware import AuthMiddleware
from systemdesign.authentication_framework.services import AuthService

app = Flask(__name__)
secret_key = "your_secret_key"
auth_service = AuthService(secret_key)
auth_middleware = AuthMiddleware(auth_service)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    try:
        user = auth_service.register_user(username, email, password)
        return jsonify({'message': 'User registered successfully', 'user_id': user.user_id}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    try:
        token = auth_service.login_user(username, password)
        return jsonify({'token': token}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@app.route('/protected', methods=['GET'])
@auth_middleware.token_required
def protected(current_user):
    return jsonify({'message': f'Welcome {current_user.username}'})

if __name__ == '__main__':
    app.run(debug=True)
