from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from routes.form.ProductForm import ProductPath, CreateProductBody, UpdateProductBody, UpdateProductNameBody, UpdateProductSlugBody, UpdateProductCategoryIdBody, UpdateProductPhotoBody, UpdateProductGalleryBody, UpdateProductPriceBody, UpdateProductStockBody, UpdateProductConditionBody, UpdateProductDetailBody, UpdateProductStatusBody

from config import Config
from utils.exception import NotFoundError
from services.ProductService import ProductService


JWT = Config.JWT

__version__ = "/v1"
__bp__ = "/products"
url_prefix = __version__ + __bp__
tag = Tag(name="Product", description="Product API")
product_bp = APIBlueprint(__bp__, __name__, url_prefix=url_prefix, abp_tags=[tag], abp_security=JWT)

class ProductForm:
    def __init__(self):
        data = request.get_json()
        self.product_slug = data.get('product_slug')
        self.product_photo = data.get('product_photo')
        self.product_gallery = data.get('product_gallery')
        self.product_name = data.get('product_name')
        self.product_price = data.get('product_price')
        self.product_stock = data.get('product_stock')
        self.product_condition = data.get('product_condition')
        self.product_detail = data.get('product_detail')
        self.status = data.get('status')
        self.seller_id = data.get('seller_id')
        self.category_id = data.get('category_id')
        
@product_bp.post('/create')
@jwt_required()
def api_create_products(body: CreateProductBody):
    try:
        form = ProductForm()
        product = ProductService.create_products(
            form.product_slug,
            form.product_photo,
            form.product_gallery,
            form.product_name,
            form.product_price,
            form.product_stock,
            form.product_condition,
            form.product_detail,
            form.status,
            form.seller_id,
            form.category_id
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

@product_bp.get('/all')
def api_get_all_products():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    product = ProductService.get_all_products(sort, order)
    return jsonify({
        'status': 200,
        'data': product
    }) if product else ('', 404)

@product_bp.get('/<int:id>')
@jwt_required()
def api_get_product_by_id(path: ProductPath):
    try:
        product = ProductService.get_product_by_id(path.id)
        return jsonify({
            'status': 200,
            'data': product
        }) if product else ('', 404)

    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@product_bp.put('/<int:id>')
@jwt_required()
def api_update_product_by_id(path: ProductPath, body: UpdateProductBody):
    try:
        form = ProductForm()
        product = ProductService.update_product(
            path.id,
            form.product_slug, 
            form.product_photo, 
            form.product_gallery,
            form.product_name, 
            form.product_price, 
            form.product_stock, 
            form.product_condition, 
            form.product_detail, 
            form.status,
            form.category_id
        )
        return jsonify({
            'message': 'Product updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404
    
@product_bp.patch('/<int:id>/category_id')
@jwt_required()
def api_update_product_category_id(path: ProductPath, body: UpdateProductCategoryIdBody):
    try:
        form = ProductForm()
        product = ProductService.update_product_category_id(
            path.id, 
            form.category_id
        )
        return jsonify({
            'message': 'Product category id updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404
    
@product_bp.patch('/<int:id>/product_slug')
@jwt_required()
def api_update_product_slug(path: ProductPath, body: UpdateProductSlugBody):
    try:
        form = ProductForm()
        product = ProductService.update_product_slug(
            path.id, 
            form.product_slug
        )
        return jsonify({
            'message': 'Product slug updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404
    
@product_bp.patch('/<int:id>/product_photo')
@jwt_required()
def api_update_product_photo(path: ProductPath, body: UpdateProductPhotoBody):
    try:
        form = ProductForm()
        product = ProductService.update_product_photo(
            path.id, 
            form.product_photo
        )
        return jsonify({
            'message': 'Product photo updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404
    
@product_bp.patch('/<int:id>/product_gallery')
@jwt_required()
def api_update_product_gallery(path: ProductPath, body: UpdateProductGalleryBody):
    try:
        form = ProductForm()
        product = ProductService.update_product_gallery(
            path.id, 
            form.product_gallery
        )
        return jsonify({
            'message': 'Product gallery updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404

@product_bp.patch('/<int:id>/product_name')
@jwt_required()
def api_update_product_name(path: ProductPath, body: UpdateProductNameBody):
    try:
        form = ProductForm()
        product = ProductService.update_product_name(
            path.id, 
            form.product_name
        )
        return jsonify({
            'message': 'Product name updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404
    
@product_bp.patch('/<int:id>/product_price')
@jwt_required()
def api_update_product_price(path: ProductPath, body: UpdateProductPriceBody):
    try:
        form = ProductForm()
        product = ProductService.update_product_price(
            path.id, 
            form.product_price
        )
        return jsonify({
            'message': 'Product price updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404

@product_bp.patch('/<int:id>/product_stock')
@jwt_required()
def api_update_product_stock(path: ProductPath, body: UpdateProductStockBody):
    try:
        form = ProductForm()
        product = ProductService.update_product_stock(
            path.id, 
            form.product_stock
        )
        return jsonify({
            'message': 'Product stock updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404

@product_bp.patch('/<int:id>/product_condition')
@jwt_required()
def api_update_product_condition(path: ProductPath, body: UpdateProductConditionBody):
    try:
        form = ProductForm()
        product = ProductService.update_product_condition(
            path.id, 
            form.product_condition
        )
        return jsonify({
            'message': 'Product condition updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404

@product_bp.patch('/<int:id>/product_detail')
@jwt_required()
def api_update_product_detail(path: ProductPath, body: UpdateProductDetailBody):
    try:
        form = ProductForm()
        product = ProductService.update_product_detail(
            path.id, 
            form.product_detail
        )
        return jsonify({
            'message': 'Product detail updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404
    
@product_bp.patch('/<int:id>/status')
@jwt_required()
def api_update_product_status(path: ProductPath, body: UpdateProductStatusBody):
    try:
        form = ProductForm()
        product = ProductService.update_product_status(
            path.id, 
            form.status
        )
        return jsonify({
            'message': 'Product status updated successfully',
            'status': 200,
            'data': product
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404

@product_bp.delete('/<int:id>')
@jwt_required()
def api_delete_product_by_id(path: ProductPath):
    try:
        ProductService.delete_product(path.id)
        return jsonify({
            'message': 'Product deleted successfully',
            'status': 200
            }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404