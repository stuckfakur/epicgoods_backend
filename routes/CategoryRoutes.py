from flask import Blueprint, request, jsonify
from services.CategoryService import CategoryService

category_bp = Blueprint('category_bp', __name__)

class CategoryForm:
    def __init__(self):
        data = request.get_json()
        self.category_name = data.get('category_name')
        self.description = data.get('description')

@category_bp.route('/category', methods=['GET'])
def api_get_category():
    category = CategoryService.get_all_category()
    return jsonify({
        'status': 200,
        'data': category
    }) if category else ('', 404)

@category_bp.route('/category', methods=['POST'])
def api_create_category():
    form = CategoryForm()
    category = CategoryService.create_category(
        form.category_name,
        form.description
    )
    return jsonify({
        'status': 201,
        'data': category.to_dict()
    }) if category else ('', 400)