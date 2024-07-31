from flask import Blueprint, request, jsonify
from services.UserService import UserService

user_bp = Blueprint('user_bp', __name__)


class UserForm:
    def __init__(self):
        data = request.get_json()
        self.username = data.get('username')


@user_bp.route('/users', methods=['GET'])
def api_get_users():
    users = UserService.get_all_users()
    return jsonify({
        'status': 200,
        'data': users
    }) if users else ('', 404)
