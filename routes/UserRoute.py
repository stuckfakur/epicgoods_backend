from flask import Blueprint, request, jsonify
from services.UserService import UserService
from flask_jwt_extended import jwt_required
from utils.exception import NotFoundError

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

@user_bp.route('/users', methods=['GET'])
@jwt_required()
def api_get_all_users():
    users = UserService.get_all_users()
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 404)

@user_bp.route('/users/<int:id>', methods=['GET'])
@jwt_required()
def api_get_users_by_id(id):
    users = UserService.get_users_by_id(id)
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 400)

@user_bp.route('/users/data', methods=['GET'])
@jwt_required()
def api_get_mydata_user():
    users = UserService.get_mydata_user()
    return jsonify({
        'status': 200,
        'data': users.to_dict()
    }) if users else ('', 404)

@user_bp.route("/users/<int:id>", methods=["PUT"])
@jwt_required()
def api_update_users(id):
    try:
        form = UserForm()
        users_updated = UserService.update_users(
            id,
            form.name,
            form.password
        )
        return jsonify({
            'message': 'User updated successfully',
            'status': 201,
            'data': users_updated.to_dict()
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

@user_bp.route('/users/<int:id>/password', methods=['PATCH'])
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

