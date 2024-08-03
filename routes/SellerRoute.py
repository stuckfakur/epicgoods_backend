from flask import Blueprint, request, jsonify
from services.SellerService import SellerService

seller_bp = Blueprint('seller_bp', __name__)


class SellerForm:
    def __init__(self):
        data = request.get_json()
        self.store_name = data.get('store_name')
        self.store_info = data.get('store_info')
        self.description = data.get('description')


@seller_bp.route('/seller', methods=['GET'])
def api_get_users():
    seller = SellerService.get_all_seller()
    return jsonify({
        'status': 200,
        'data': seller
    }) if seller else ('', 404)

@seller_bp.route('/seller', methods=['POST'])
def api_create_users():
    form = SellerForm()
    seller = SellerService.create_seller(
        form.store_name,
        form.store_info,
        form.description
    )
    return jsonify({
        'status': 201,
        'data': seller.to_dict()
    }) if seller else ('', 400)