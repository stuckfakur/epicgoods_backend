from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from routes.form.VoucherForm import VoucherPath, CreateVoucherBody, UpdateVoucherBody, UpdateVoucherName, UpdateVoucherCode, UpdateVoucherType, UpdateVoucherValue, UpdateVoucherQuota

from config import Config
from utils.exception import NotFoundError
from services.VoucherService import VoucherService

JWT = Config.JWT

__version__ = "/v1"
__bp__ = "/vouchers"
url_prefix = __version__ + __bp__
tag = Tag(name="Voucher", description="Voucher API")
voucher_bp = APIBlueprint(__bp__, __name__, url_prefix=url_prefix, abp_tags=[tag], abp_security=JWT)

class VoucherForm:
    def __init__(self):
        data = request.get_json()
        self.voucher_name = data.get('voucher_name')
        self.voucher_code = data.get('voucher_code')
        self.voucher_type = data.get('voucher_type')
        self.voucher_value = data.get('voucher_value')
        self.voucher_quota = data.get('voucher_quota')

@voucher_bp.post('/create')
@jwt_required()
def api_create_voucher(body: CreateVoucherBody):
    try:
        form = VoucherForm()
        voucher = VoucherService.create_voucher(
            form.voucher_name,
            form.voucher_code,
            form.voucher_type,
            form.voucher_value,
            form.voucher_quota
        )
        return jsonify({
            'message': 'Voucher created successfully',
            'status': 201,
            'data': voucher.to_dict()
        }),
    except ValueError as e:
        return jsonify({'error' : {
            'message': str(e),
            'status': 400
        }}), 400

@voucher_bp.get('/all')
@jwt_required()
def api_get_all_vouchers():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')
    
    voucher = VoucherService.get_all_voucher(sort, order)
    return jsonify({
        'status': 200,
        'data': voucher
    }) if voucher else ('', 404)

@voucher_bp.get('/<int:id>')
@jwt_required()
def api_get_voucher_by_id(path: VoucherPath):
    voucher = VoucherService.get_voucher_by_id(path.id)
    return jsonify({
        'status': 200,
        'data': voucher
    }) if voucher else ('', 404)

@voucher_bp.put('/<int:id>')
@jwt_required()
def api_update_voucher(path: VoucherPath, body: UpdateVoucherBody):
    try:
        form = VoucherForm()
        voucher = VoucherService.update_voucher(
            path.id, 
            form.voucher_name,
            form.voucher_code,
            form.voucher_type,
            form.voucher_value, 
            form.voucher_quota
        )
        return jsonify({
            'message': 'Voucher updated successfully',
            'status': 200,
            'data': voucher.to_dict()
        }), 200
    except ValueError as e:
        return jsonify({'error' : {
            'message': str(e),
            'status': 400
        }}), 400

