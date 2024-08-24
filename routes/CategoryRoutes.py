import os

from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from routes.form.CategoryForm import CategoryPath, CreateBody, UpdateBody, UpdateCategorySlugBody, \
    UpdateCategoryNameBody, UpdateCategoryDescriptionBody, CategoryDetailResponse

from config import Config
from services.CategoryService import CategoryService
from utils.exception import NotFoundError

JWT = Config.JWT

__version__ = "/v1"
__bp__ = "/categories"
url_prefix = __version__ + __bp__
tag = Tag(name="Category", description="Category API")
category_bp = APIBlueprint(__bp__, __name__, url_prefix=url_prefix, abp_tags=[tag], abp_security=JWT)


class CategoryForm:
    def __init__(self):
        data = request.get_json()
        self.category_slug = data.get('category_slug')
        self.category_name = data.get('category_name')
        self.category_photo = data.get('category_photo')
        self.description = data.get('description')


@category_bp.post("/create")
@jwt_required()
def api_create_category(body: CreateBody):
    try:
        form = CategoryForm()
        category = CategoryService.create_category(
            form.category_slug,
            form.category_name,
            form.category_photo,
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


@category_bp.get("/all")
def api_get_all_category():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    category = CategoryService.get_all_category(sort, order)

    return jsonify({
        'status': 200,
        'data': category
    }) if category else ('', 404)


@category_bp.get("/<int:id>")
@jwt_required()
def api_get_category_by_id(path: CategoryPath):
    try:
        category = CategoryService.get_category_by_id(path.id)
        return jsonify({
            'status': 200,
            'data': category
        }) if category else ('', 404)

    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404


@category_bp.put("/<int:id>")
@jwt_required()
def api_update_category(path: CategoryPath, body: UpdateBody):
    try:
        form = CategoryForm()
        category_updated = CategoryService.update_category(
            path.id, form.category_slug, form.category_name, form.category_photo, form.description)
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


@category_bp.patch("/<int:id>/category_slug")
@jwt_required()
def api_update_category_slug(path: CategoryPath, body: UpdateCategorySlugBody):
    try:
        form = CategoryForm()
        category = CategoryService.update_category_slug(
            path.id,
            form.category_slug
        )
        return jsonify({
            'message': 'Category slug updated successfully',
            'status': 201,
            'data': category.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404


@category_bp.patch("/<int:id>/category_name")
@jwt_required()
def api_update_category_name(path: CategoryPath, body: UpdateCategoryNameBody):
    try:
        form = CategoryForm()
        category = CategoryService.update_category_name(
            path.id,
            form.category_name
        )
        return jsonify({
            'message': 'Category slug updated successfully',
            'status': 201,
            'data': category.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404

@category_bp.patch("/<int:id>/description")
@jwt_required()
def api_update_category_description(path: CategoryPath, body: UpdateCategoryDescriptionBody):
    try:
        form = CategoryForm()
        category = CategoryService.update_category_description(
            path.id,
            form.description
        )
        return jsonify({
            'message': 'Category description updated successfully',
            'status': 201,
            'data': category.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 400
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e)
        }}), 404
    
@category_bp.delete("/<int:id>")
@jwt_required()
def api_delete_category(path: CategoryPath):
    try:
        CategoryService.delete_category(path.id)
        return jsonify({
            'message': 'Category deleted successfully',
            'status': 200
        }), 200

    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404
