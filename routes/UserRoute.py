from flask import Blueprint, request

user_bp = Blueprint('user_bp', __name__)


class UserForm:
    def __init__(self):
        data = request.get_json()
        self.username = data.get('username')


@user_bp.route('/users', methods=['GET'])
def api_get_users():
    return "make function to get user here"
