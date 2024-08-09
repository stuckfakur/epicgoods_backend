from flask import Blueprint, request, jsonify
from services.FollowerService import FollowerService

follower_bp = Blueprint('follower_bp', __name__)

class FollowerForm:
    def __init__(self):
        data = request.get_json()
        self.user_id = data.get('user_id')
        self.followers_id = data.get('followers_id')
        
@follower_bp.route('/follower', methods=['GET'])
def api_get_follower():
    follower = FollowerService.get_all_follower()
    return jsonify({
        'status': 200,
        'data': follower
    }) if follower else ('', 404)

@follower_bp.route('/follower', methods=['POST'])
def api_create_follower():
    form = FollowerForm()
    follower = FollowerService.create_follower(
        form.user_id,
        form.followers_id
    )
    return jsonify({
        'status': 201,
        'data': follower.to_dict()
    }) if follower else ('', 400)