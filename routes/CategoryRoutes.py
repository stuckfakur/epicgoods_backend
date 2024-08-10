from flask import Blueprint, request, jsonify
from services.CategoryService import CategoryService
from flask_jwt_extended import jwt_required
from utils.exception import NotFoundError

category_bp = Blueprint('category_bp', __name__)

class CategoryForm:
    def __init__(self):
        data = request.get_json()
        self.category_slug = data.get('category_slug')
        self.category_name = data.get('category_name')
        self.description = data.get('description')

@category_bp.route('/categories', methods=['POST'])
@jwt_required()
def api_create_category():
    try:
        form = CategoryForm()
        category = CategoryService.create_category(
            form.category_slug,
            form.category_name,
            form.description
        )
        return jsonify({
            'message': 'Category created successfully',
            'status': 201,
            'data': category.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({
            'message': str(e),
            'status': 400
        }), 400

@category_bp.route('/categories', methods=['GET'])
@jwt_required()
def api_get_all_category():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    category = CategoryService.get_all_category(sort, order)

    return jsonify({
        'status': 200,
        'data': category
    }) if category else ('', 404)


@category_bp.route('/categories/<int:id>', methods=['GET'])
@jwt_required()
def api_get_category_by_id(id):
    try:
        category = CategoryService.get_category_by_id(id)
        return jsonify({
            'status': 200,
            'data': category
        }) if category else ('', 404)

    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@category_bp.route('/categories/<int:id>', methods=['PUT'])
@jwt_required()
def api_update_category(id):
    try:
        form = CategoryForm()
        category_updated = CategoryService.update_category(id, form.category_slug, form.category_name, form.description)
        return jsonify({
            'message': 'Category updated successfully',
            'status': 200,
            'data': category_updated.to_dict()
        }), 200
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404
    
@category_bp.route('/categories/<int:id>', methods=['DELETE'])
@jwt_required()
def api_delete_category(id):
    try:
        CategoryService.delete_category(id)
        return jsonify({
            'message': 'Category deleted successfully', 
            'status': 200
        }) ,200
    
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e), 
            'status': 404
        }}), 404