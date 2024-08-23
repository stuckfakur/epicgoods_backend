from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from routes.form.ProductCartForm import *

from config import Config
from utils.exception import NotFoundError
from services.ProductCartService import ProductCartService

JWT = Config.JWT

__version__ = "/v1"
__bp__ = "/product_carts"
url_prefix = __version__ + __bp__
tag = Tag(name="Product Cart", description="Product Cart API")
product_cart_bp = APIBlueprint(__bp__, __name__, url_prefix=url_prefix, abp_tags=[tag], abp_security=JWT)


class ProductCartForm:
    def __init__(self):
        data = request.get_json()
        self.user_id = data.get('user_id')
        self.product_id = data.get('product_id')
        self.quantity = data.get('quantity')

@product_cart_bp.post('/create')
@jwt_required()
def api_create_product_cart(body: BaseProductCartBody):
    try:
        form = ProductCartForm()
        product_cart = ProductCartService.create_product_cart(
            form.user_id,
            form.product_id,
            form.quantity
        )
        return jsonify({
            'message': 'Product cart created successfully',
            'status' : 201,
            'data': product_cart.to_dict()            
        })
    except ValueError as e:
        return jsonify({'error' : {
            'messege' : str(e),
            'status': 400
        }}), 400
    
@product_cart_bp.get('/all')
@jwt_required()
def api_get_all_product_cart():
    product_cart = ProductCartService.get_all_product_cart()
    return jsonify({
        'status': 200,
        'data': product_cart
    }) if product_cart else ('', 404)

@product_cart_bp.get('/<int:id>')
@jwt_required()
def api_get_product_cart_by_id(path: ProductCartPath):
    product_cart = ProductCartService.get_product_cart_by_id(path.id)
    return jsonify({
        'status': 200,
        'data': product_cart
    }) if product_cart else ('', 404)

@product_cart_bp.put('/<int:id>')
@jwt_required()
def api_update_product_cart(path: ProductCartPath, body: UpdateProductCartBody):
    try:
        form = ProductCartForm()
        product_cart = ProductCartService.update_product_cart(
            path.id,
            form.product_id,
            form.quantity
        )
        return jsonify({
            'messege': 'Product cart update successfully',
            'status': 201,
            'data': product_cart
        }), 200
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400
    
@product_cart_bp.patch('/<int:id>/product_id')
@jwt_required()
def api_update_product_cart_product_id(path: ProductCartPath, body: UpdateProductIdBody):
    try:
        form = ProductCartForm()
        product_cart = ProductCartService.update_product_cart_product_id(
            path.id,
            form.product_id
        )
        return jsonify({
            'message': 'Product id update successfully',
            'status': 201,
            'data': product_cart.to_dict()
        }), 200
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404
    
@product_cart_bp.patch('/<int:id>/quantity')
@jwt_required()
def api_update_product_cart_quantity(path: ProductCartPath, body: UpdateProductQuantityBody):
    try:
        form = ProductCartForm()
        product_cart = ProductCartService.update_product_cart_quantity(
            path.id,
            form.quantity
        )
        return jsonify({
            'message': 'Quantity update successfully',
            'status': 201,
            'data': product_cart.to_dict()
        }), 200
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404