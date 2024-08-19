import os

from flasgger import swag_from
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from routes.form.UserForm import UserPath, CreateUserBody, UpdateUserBody, UpdateUserStatusBody, UpdateUserPasswordBody, UpdateUserIsSellerBody

from config import Config
from utils.exception import NotFoundError
from services.UserService import UserService


JWT = Config.JWT

__version__ = "/v1"
__bp__ = "/users"
url_prefix = __version__ + __bp__
tag = Tag(name="User", description="User API")
user_bp = APIBlueprint(__bp__, __name__, url_prefix=url_prefix, abp_tags=[tag], abp_security=JWT)

class UserForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.username = data.get('username')
        self.email = data.get('email')
        self.status = data.get('status')
        self.password = data.get('password')
        self.consumer_data = data.get('consumer_data')
        self.is_seller = data.get('is_seller')
@user_bp.post("/create")
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/CreateUser.yml'))
def api_create_users(body: CreateUserBody):
    try:
        user_form = UserForm()
        user = UserService.create_users(
            user_form.name,
            user_form.email,
            user_form.password,
        )

        return jsonify({
            'message': 'user successfully registered',
            'status': 200,
            'data': user.to_dict()
        }), 200
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400

@user_bp.get("/all")
@jwt_required()
def api_get_all_users():
    users = UserService.get_all_users()
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 404)

@user_bp.get("/<int:id>")
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/GetUserById.yml'))
def api_get_users_by_id(path: UserPath):
    users = UserService.get_users_by_id(path.id)
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 400)

@user_bp.get("/data")
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/GetMyDataUser.yml'))
def api_get_mydata_user():
    users = UserService.get_mydata_user()
    return jsonify({
        'status': 200,
        'data': users.to_dict()
    }) if users else ('', 404)

@user_bp.put("/<int:id>")
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/UpdateUser.yml'))
def api_update_users(path: UserPath, body: UpdateUserBody):
    try:
        form = UserForm()
        user = UserService.update_users(
            path.id,
            form.name,
            form.username,
            form.email,
            form.password,
            form.status,
            form.consumer_data,
        )
        return jsonify({
            'message': 'User updated successfully',
            'status': 201,
            'data': user
        }), 200
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404

@user_bp.patch('/<int:id>/status')
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/UpdateUserStatus.yml'))
def api_update_user_status(path: UserPath, body: UpdateUserStatusBody):
    try:
        form = UserForm()
        user = UserService.update_users_status(
            path.id,
            form.status
        )
        return jsonify({
            'message': 'user status updated successfully',
            'status': 201,
            'data': user.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404
    
@user_bp.patch("/<int:id>/is_seller")
@jwt_required()
def api_update_user_is_seller(path: UserPath, body: UpdateUserIsSellerBody):
    try:
        form = UserForm()
        user = UserService.update_users_is_seller(
            path.id,
            form.is_seller
        )
        return jsonify({
            'message': 'user is_seller updated successfully',
            'status': 201,
            'data': user.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@user_bp.patch("/<int:id>/password")
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/UpdateUserPassword.yml'))
def api_update_user_password(path: UserPath, body: UpdateUserPasswordBody):
    try:
        form = UserForm()
        user = UserService.update_users_password(
            path.id,
            form.password
        )
        return jsonify({
            'message': 'user password updated successfully',
            'status': 201,
            'data': user.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@user_bp.delete("/<int:id>")
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/DeleteUser.yml'))
def api_delete_users(path: UserPath):
    try:
        UserService.delete_users(path.id)
        return jsonify({
            'message': 'User deleted successfully',
            'status': 200,
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404

