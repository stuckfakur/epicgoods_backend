from flask import Blueprint, request, jsonify, make_response 
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
from models.User import db
from services.UserService import UserService
from models.User import User, TokenBlacklist
from utils.email_register import send_email
from flasgger import swag_from
import os

auth_bp = Blueprint('auth_bp', __name__)
class UserForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.username = data.get('username')
        self.email = data.get('email')
        self.password = data.get('password')
        self.consumer_data = data.get('consumer_data')

@auth_bp.route('/register', methods=['POST'])
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/Auth/Register.yml'))
def api_register():
    try:
        user_form = UserForm()
        user = UserService.create_users(
            user_form.name,
            user_form.email,
            user_form.password,
        )
        send_email(user_form.email, user_form.name)

        return jsonify({
            'message': 'User created successfully',
            'status': 200,
            'data': user.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error':{
            'message': str(e),
            'status': 400
        }}), 400

@auth_bp.route('/login', methods=['POST'])
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/Auth/Login.yml'))
def api_login():
    data = request.get_json()

    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': {
            'message': 'Email and password are required',
        }}), 400

    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        if user.status == '1':
            additional_claims = {
                'id' : user.id,
                'name': user.name,
                'username': user.username,
                'email': user.email,
                'consumer_data': user.consumer_data
            }

            access_token = create_access_token(identity=additional_claims)
            refresh_token = create_refresh_token(identity=additional_claims)
            return jsonify(access_token=access_token, refresh_token=refresh_token), 200
        elif user.status == '0':
            return jsonify({'error': {
                'message': 'User is not active'
            }}), 400
    else:
        return jsonify({'error': {
            'message': 'Invalid Email or password'
        }}), 401
@auth_bp.route('/refresh', methods=['POST'])
def refresh_option():
    response = make_response()
    response.headers['Acces-Control-Allow-Origin'] = 'http://0.0.0.0/0'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

    return response

@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({'error': 'invalid refresh token'}), 422

    print(f'refresh token for user: {current_user}')
    new_access_token = create_access_token(identity=current_user)
    response = jsonify(access_token=new_access_token)
    response.headers['Access-Control-Allow-Origin'] = 'http://0.0.0.0/0'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/Auth/Logout.yml'))
def api_logout():
    jti = get_jwt()['jti']
    token = TokenBlacklist(jti=jti)
    db.session.add(token)
    db.session.commit()
    return jsonify(msg="Successfully logged out")