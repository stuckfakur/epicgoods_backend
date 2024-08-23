from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from config import Config
from routes.form.VoucherForm import *
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
def api_create_voucher(body: BaseVoucherBody):
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
        }), 201
    except ValueError as e:
        return jsonify({'error': {
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
            'data': voucher
        }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
        }}), 400
    
@voucher_bp.patch('/<int:id>/voucher_name')
@jwt_required()
def api_update_voucher_name(path: VoucherPath, body: UpdateVoucherName):
    try:
        form = VoucherForm()
        voucher = VoucherService.update_voucher_name(
            path.id,
            form.voucher_name
        )
        return jsonify({
            'message': 'Voucher name updated successfully',
            'status': 200,
            'data': voucher
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
    
@voucher_bp.patch('/<int:id>/voucher_code')
@jwt_required()
def api_update_voucher_code(path: VoucherPath, body: UpdateVoucherCode):
    try:
        form = VoucherForm()
        voucher = VoucherService.update_voucher_code(
            path.id,
            form.voucher_code
        )
        return jsonify({
            'message': 'Voucher code updated successfully',
            'status': 200,
            'data': voucher
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
    
@voucher_bp.patch('/<int:id>/voucher_type')
@jwt_required()
def api_update_voucher_type(path: VoucherPath, body: UpdateVoucherType):
    try:
        form = VoucherForm()
        voucher = VoucherService.update_voucher_type(
            path.id,
            form.voucher_type
        )
        return jsonify({
            'message': 'Voucher type updated successfully',
            'status': 200,
            'data': voucher
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
    
@voucher_bp.patch('/<int:id>/voucher_value')
@jwt_required()
def api_update_voucher_value(path: VoucherPath, body: UpdateVoucherValue):
    try:
        form = VoucherForm()
        voucher = VoucherService.update_voucher_value(
            path.id,
            form.voucher_value
        )
        return jsonify({
            'message': 'Voucher value updated successfully',
            'status': 200,
            'data': voucher
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
    
@voucher_bp.patch('/<int:id>/voucher_quota')
@jwt_required()
def api_update_voucher_quota(path: VoucherPath, body: UpdateVoucherQuota):
    try:
        form = VoucherForm()
        voucher = VoucherService.update_voucher_quota(
            path.id,
            form.voucher_quota
        )
        return jsonify({
            'message': 'Voucher quota updated successfully',
            'status': 200,
            'data': voucher
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

@voucher_bp.delete('/<int:id>')
@jwt_required()
def api_delete_voucher_by_id(path: VoucherPath):
    try:
        VoucherService.delete_voucher(path.id)
        return jsonify({
            'message': 'Voucher deleted successfully',
            'status': 200
            }), 200
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
            }}), 404
    except ValueError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 400
            }}), 400