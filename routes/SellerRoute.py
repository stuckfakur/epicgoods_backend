from flask import Blueprint, request, jsonify
from services.SellerService import SellerService
from flask_jwt_extended import jwt_required
from utils.exception import NotFoundError

seller_bp = Blueprint('seller_bp', __name__)


class SellerForm:
    def __init__(self):
        data = request.get_json()
        self.store_name = data.get('store_name')
        self.store_info = data.get('store_info')
        self.description = data.get('description')

@seller_bp.route('/sellers', methods=['POST'])
@jwt_required()
def api_create_seller():
    form = SellerForm()
    seller = SellerService.create_seller(
        form.store_name,
        form.store_info,
        form.description
    )
    return jsonify({
        'message': 'Seller created successfully',
        'status': 201,
        'data': seller.to_dict()
    }) if seller else ('', 400)

@seller_bp.route('/sellers', methods=['GET'])
@jwt_required()
def api_get_all_users():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')
    
    seller = SellerService.get_all_seller(sort, order)
    return jsonify({
        'status': 200,
        'data': seller
    }) if seller else ('', 404)

@seller_bp.route('/sellers/<int:seller_id>', methods=['GET'])
@jwt_required()
def api_get_seller_by_id(seller_id):
    seller = SellerService.get_seller_by_id(seller_id)
    return jsonify({
        'status': 200,
        'data': seller
    }) if seller else ('', 404)