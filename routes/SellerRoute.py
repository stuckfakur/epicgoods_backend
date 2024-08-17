from flask import Blueprint, request, jsonify
from services.SellerService import SellerService
from flask_jwt_extended import jwt_required
from utils.exception import NotFoundError

seller_bp = Blueprint('seller_bp', __name__)


class SellerForm:
    def __init__(self):
        data = request.get_json()
        self.user_id = data.get('user_id')
        self.location_id = data.get('location_id')
        self.address = data.get('address')
        self.store_name = data.get('store_name')
        self.store_type = data.get('store_type')
        self.store_info = data.get('store_info')
        self.description = data.get('description')

@seller_bp.route('/sellers', methods=['POST'])
@jwt_required()
def api_create_seller():
    try:
        form = SellerForm()
        seller = SellerService.create_seller(
            form.user_id,
            form.location_id,
            form.address,
            form.store_name,
            form.store_info,
            form.description,
        )
        return jsonify({
            'message': 'Seller created successfully',
            'status': 201,
            'data' : seller.to_dict()
        })
    except ValueError as e:
        return jsonify({'error' : {
            'messege' : str(e),
            'status': 400
        }}), 400

@seller_bp.route('/sellers', methods=['GET'])
@jwt_required()
def api_get_all_seller():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')
    
    seller = SellerService.get_all_seller(sort, order)
    return jsonify({
        'status': 200,
        'data': seller
    }) if seller else ('', 404)

@seller_bp.route('/sellers/<int:id>', methods=['GET'])
@jwt_required()
def api_get_seller_by_id(id):
    seller = SellerService.get_seller_by_id(id)
    return jsonify({
        'status': 200,
        'data': seller
    }) if seller else ('', 404)

@seller_bp.route('/sellers/<int:id>', methods=['PUT'])
@jwt_required()
def api_update_sellers(id):
    try:
        form = SellerForm()
        seller = SellerService.update_seller(
            id,
            form.location_id,
            form.address,
            form.store_name,
            form.store_type,
            form.store_info,
            form.description
        )
        return jsonify({
            'messege': 'User update successfully',
            'status': 201,
            'data': seller
        }), 200
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400
    
@seller_bp.route("/sellers/<int:id>", methods=["DELETE"])
@jwt_required()
def api_delete_sellers(id):
    try:
        SellerService.delete_seller(id)
        return jsonify({
            'message': 'Seller deleted successfully',
            'status': 200,
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404
