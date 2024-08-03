from flask import Blueprint, request, jsonify
from services.UserService import UserService

user_bp = Blueprint('user_bp', __name__)


class UserForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.username = data.get('username')
        self.email = data.get('email')
        self.password = data.get('password')
        self.consumer_data = data.get('consumer_data')


@user_bp.route('/users', methods=['GET'])
def api_get_users():
    users = UserService.get_all_users()
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 404)

@user_bp.route('/users', methods=['POST'])
def api_create_users():
    form = UserForm()
    users = UserService.create_users(
        form.name,
        form.username,
        form.email,
        form.password,
        form.consumer_data
    )
    return jsonify({
        'status': 201,
        'data': users.to_dict()
    }) if users else ('', 400)

@user_bp.route('/users/<int:id>', methods=['GET'])
def api_get_users_by_id(id):
    users = UserService.get_users(id)
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 400)

@user_bp.route("/users/<int:id>", methods=["DELETE"])
def api_delete_users(id):
    users = UserService.delete_users(id)
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 400)

@user_bp.route("/users/<int:id>", methods=["PUT"])
def api_update_users(id):
    users = UserService.update_users(id)
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 400)