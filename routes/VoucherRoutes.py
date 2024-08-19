from flask import Blueprint, request, jsonify
from services.VoucherService import VoucherService
from flask_jwt_extended import jwt_required

voucher_bp = Blueprint('voucher_bp', __name__)

class VoucherForm:
    def __init__(self):
        data = request.get_json()
        self.voucher_name = data.get('voucher_name')
        self.voucher_code = data.get('voucher_code')
        self.voucher_type = data.get('voucher_type')
        self.voucher_value = data.get('voucher_value')
        self.voucher_quota = data.get('voucher_quota')

@voucher_bp.route('/vouchers', methods=['POST'])
@jwt_required()
def api_create_voucher():
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


