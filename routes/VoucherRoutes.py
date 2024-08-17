from flask import Blueprint, request, jsonify
from services.SellerService import SellerService
from flask_jwt_extended import jwt_required
from utils.exception import NotFoundError

voucher_bp = Blueprint('voucher_bp', __name__)

class VoucherForm:
    def __init__(self):
        data = request.get_json()
        self.name = data.get('name')
        self.code = data.get('code')
        self.type = data.get('type')
        self.value = data.get('value')
        self.quota = data.get('quota')

@voucher_bp.route('/vouchers', methods=['POST'])
@jwt_required()
def api_create_voucher():
    try:
        form = VoucherForm()
        voucher = VoucherService.create_voucher(
            form.name,
            form.code,
            form.type,
            form.value,
            form.quota
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


