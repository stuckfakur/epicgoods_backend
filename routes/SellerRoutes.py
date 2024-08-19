from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from routes.form.SellerForm import CreateSellerBody, UpdateSellerBody, SellerPath, UpdateSellerLocationIdBody, UpdateSellerAddressBody, UpdateSellerStoreNameBody, UpdateSellerStoreInfoBody, UpdateSellerDescriptionBody, UpdateSellerStoreTypeBody

from config import Config
from utils.exception import NotFoundError
from services.SellerService import SellerService

JWT = Config.JWT

__version__ = "/v1"
__bp__ = "/sellers"
url_prefix = __version__ + __bp__
tag = Tag(name="Seller", description="Seller API")
seller_bp = APIBlueprint(__bp__, __name__, url_prefix=url_prefix, abp_tags=[tag], abp_security=JWT)


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

@seller_bp.post('/create')
@jwt_required()
def api_create_seller(body: CreateSellerBody):
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

@seller_bp.get('/all')
@jwt_required()
def api_get_all_seller():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')
    
    seller = SellerService.get_all_seller(sort, order)
    return jsonify({
        'status': 200,
        'data': seller
    }) if seller else ('', 404)

@seller_bp.get('/<int:id>')
@jwt_required()
def api_get_seller_by_id(path: SellerPath):
    seller = SellerService.get_seller_by_id(path.id)
    return jsonify({
        'status': 200,
        'data': seller
    }) if seller else ('', 404)

@seller_bp.put('/<int:id>')
@jwt_required()
def api_update_sellers(path: SellerPath, body: UpdateSellerBody):
    try:
        form = SellerForm()
        seller = SellerService.update_seller(
            path.id,
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

@seller_bp.patch('/<int:id>/location_id')
@jwt_required()
def api_update_seller_location_id(path: SellerPath, body: UpdateSellerLocationIdBody):
    try:
        form = SellerForm()
        seller = SellerService.update_seller_location_id(
            path.id,
            form.location_id
        )
        return jsonify({
            'message': 'seller location_id updated successfully',
            'status': 201,
            'data': seller.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404
    
@seller_bp.patch('/<int:id>/address')
@jwt_required()
def api_update_seller_address(path: SellerPath, body: UpdateSellerAddressBody):
    try:
        form = SellerForm()
        seller = SellerService.update_seller_address(
            path.id,
            form.address
        )
        return jsonify({
            'message': 'seller address updated successfully',
            'status': 201,
            'data': seller.to_dict()
        }), 201
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400

@seller_bp.patch('/<int:id>/store_name')
@jwt_required()
def api_update_seller_store_name(path: SellerPath, body: UpdateSellerStoreNameBody):
    try:
        form = SellerForm()
        seller = SellerService.update_seller_store_name(
            path.id,
            form.store_name
        )
        return jsonify({
            'message': 'seller store_name updated successfully',
            'status': 201,
            'data': seller.to_dict()
        }), 201
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    
@seller_bp.patch('/<int:id>/store_type')
@jwt_required()
def api_update_seller_store_type(path: SellerPath, body: UpdateSellerStoreTypeBody):
    try:
        form = SellerForm()
        seller = SellerService.update_seller_store_type(
            path.id,
            form.store_type
        )
        return jsonify({
            'message': 'seller store_type updated successfully',
            'status': 201,
            'data': seller.to_dict()
        }), 201
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400

@seller_bp.patch('/<int:id>/store_info')
@jwt_required()
def api_update_seller_store_info(path: SellerPath, body: UpdateSellerStoreInfoBody):
    try:
        form = SellerForm()
        seller = SellerService.update_seller_store_info(
            path.id,
            form.store_info
        )
        return jsonify({
            'message': 'seller store_info updated successfully',
            'status': 201,
            'data': seller.to_dict()
        }), 201
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400

@seller_bp.patch('/<int:id>/description')
@jwt_required()
def api_update_seller_description(path: SellerPath, body: UpdateSellerDescriptionBody):
    try:
        form = SellerForm()
        seller = SellerService.update_seller_description(
            path.id,
            form.description
        )
        return jsonify({
            'message': 'seller description updated successfully',
            'status': 201,
            'data': seller.to_dict()
        }), 201
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400

@seller_bp.delete("/<int:id>")
@jwt_required()
def api_delete_sellers(path: SellerPath):
    try:
        SellerService.delete_seller(path.id)
        return jsonify({
            'message': 'Seller deleted successfully',
            'status': 200,
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404
