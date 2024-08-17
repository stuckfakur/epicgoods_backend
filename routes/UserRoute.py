from flask import Blueprint, request, jsonify
from services.UserService import UserService
from flask_jwt_extended import jwt_required
from utils.exception import NotFoundError
from flasgger import swag_from
import os

user_bp = Blueprint('user_bp', __name__)

class UserForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.username = data.get('username')
        self.email = data.get('email')
        self.status = data.get('status')
        self.password = data.get('password')
        self.consumer_data = data.get('consumer_data')

@user_bp.route('/users', methods=['POST'])
@jwt_required()
def api_create_users():
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

@user_bp.route('/users', methods=['GET'])
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/GetAllUsers.yml'))
def api_get_all_users():
    users = UserService.get_all_users()
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 404)

@user_bp.route('/users/<int:id>', methods=['GET'])
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/GetUserById.yml'))
def api_get_users_by_id(id):
    users = UserService.get_users_by_id(id)
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 400)

@user_bp.route('/users/data', methods=['GET'])
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/GetMyDataUser.yml'))
def api_get_mydata_user():
    users = UserService.get_mydata_user()
    return jsonify({
        'status': 200,
        'data': users.to_dict()
    }) if users else ('', 404)

@user_bp.route("/users/<int:id>", methods=["PUT"])
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/UpdateUser.yml'))
def api_update_users(id):
    try:
        form = UserForm()
        user = UserService.update_users(
            id,
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

@user_bp.route('/users/<int:id>/status', methods=['PATCH'])
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/UpdateUserStatus.yml'))
def api_update_user_status(id):
    try:
        form = UserForm()
        user = UserService.update_users_status(
            id,
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
    
@user_bp.route('/users/<int:id>/is_seller', methods=['PATCH'])
@jwt_required()
def api_update_user_is_seller(id):
    try:
        form = UserForm()
        user = UserService.update_users_is_seller(
            id,
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

@user_bp.route('/users/<int:id>/password', methods=['PATCH'])
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/UpdateUserPassword.yml'))
def api_update_user_password(id):
    try:
        form = UserForm()
        user = UserService.update_users_password(
            id,
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

@user_bp.route("/users/<int:id>", methods=["DELETE"])
@jwt_required()
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/User/DeleteUser.yml'))
def api_delete_users(id):
    try:
        UserService.delete_users(id)
        return jsonify({
            'message': 'User deleted successfully',
            'status': 200,
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404

