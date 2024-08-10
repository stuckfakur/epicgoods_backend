from flask import Blueprint, request, jsonify
from services.ProductService import ProductService
from flask_jwt_extended import jwt_required
from utils.exception import NotFoundError

product_bp = Blueprint('product_bp', __name__)

class ProductForm:
    def __init__(self):
        data = request.get_json()
        self.product_slug = data.get('product_slug')
        self.product_photo = data.get('product_photo')
        self.product_gellery = data.get('product_gellery')
        self.product_name = data.get('product_name')
        self.product_price = data.get('product_price')
        self.product_stock = data.get('product_stock')
        self.product_condition = data.get('product_condition')
        self.product_detail = data.get('product_detail')
        self.status = data.get('status')
        self.user_id = data.get('user_id')
        self.category_id = data.get('category_id')
        
@product_bp.route('/products', methods=['POST'])
@jwt_required()
def api_create_products():
    try:
        form = ProductForm()
        product = ProductService.create_products(
            form.product_slug,
            form.product_photo,
            form.product_gellery,
            form.product_name,
            form.product_price,
            form.product_stock,
            form.product_condition,
            form.product_detail,
            form.status
        )
        return jsonify({
            'message': 'Successfully created product',
            'status': 201,
            'data': product.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({
            'message': str(e),
            'status': 400
        }), 400

@product_bp.route('/products', methods=['GET'])
def api_get_all_products():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    product = ProductService.get_all_products(sort, order)
    return jsonify({
        'status': 200,
        'data': product
    }) if product else ('', 404)

@product_bp.route('/products/<int:id>', methods=['GET'])
@jwt_required()
def api_get_product_by_id(id):
    try:
        product = ProductService.get_product_by_id(id)
        return jsonify({
            'status': 200,
            'data': product
        }) if product else ('', 404)

    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@product_bp.route('/products/<int:id>', methods=['DELETE'])
@jwt_required()
def api_delete_product_by_id(id):
    try:
        ProductService.delete_product(id)
        return jsonify({
            'message': 'Product deleted successfully',
            'status': 200
            }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404

