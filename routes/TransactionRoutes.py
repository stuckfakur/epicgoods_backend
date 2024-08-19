from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from services.TransactionService import TransactionService

transaction_bp = Blueprint('transaction_bp', __name__)

class TransactionForm:
    def __init__(self):
        data = request.get_json()
        self.stock_id = data.get('stock_id')
        self.voucher_id = data.get('voucher_id')
        self.quantity = data.get('quantity')
        self.total_price = data.get('total_price')

@transaction_bp.route('/transactions', methods=['POST'])
def api_create_transaction():
    try:
        form = TransactionForm()
        transaction = TransactionService.create_transaction(
            form.stock_id, 
            form.voucher_id, 
            form.quantity, 
            form.total_price
        )
        return jsonify({
            'message': 'Transaction created successfully', 
            'status': 201, 
            'data': transaction.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({'error' : {
            'message': str(e),
            'status': 400
            }}), 400