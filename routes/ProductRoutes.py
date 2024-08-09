from flask import Blueprint, request, jsonify
from services.ProductService import ProductService

product_bp = Blueprint('product_bp', __name__)


class ProductForm:
    def __init__(self):
        data = request.get_json()
        self.product_photo = data.get('product_photo')
        self.product_gellery = data.get('product_gellery')
        self.product_name = data.get('product_name')
        self.product_price = data.get('product_price')
        self.product_stock = data.get('product_stock')
        self.product_condition = data.get('product_condition')
        self.product_detail = data.get('product_detail')
        self.status = data.get('status')


@product_bp.route('/product', methods=['GET'])
def api_get_users():
    product = ProductService.get_all_product()
    return jsonify({
        'status': 200,
        'data': product
    }) if product else ('', 404)

@product_bp.route('/product', methods=['POST'])
def api_create_users():
    form = ProductForm()
    product = ProductService.create_product(
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
        'status': 201,
        'data': product.to_dict()
    }) if product else ('', 400)