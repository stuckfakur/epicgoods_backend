from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

from utils.exception import NotFoundError
from config import Config
from routes.form.TransactionForm import *
from services.TransactionService import TransactionService

JWT = Config.JWT

__version__ = "/v1"
__bp__ = "/transactions"
url_prefix = __version__ + __bp__
tag = Tag(name="Transaction", description="Transaction API")
transaction_bp = APIBlueprint(__bp__, __name__, url_prefix=url_prefix, abp_tags=[tag], abp_security=JWT)


class TransactionForm:
    def __init__(self):
        data = request.get_json()
        self.user_id = data.get('user_id')
        self.product_id = data.get('product_id')
        self.voucher_id = data.get('voucher_id')
        self.quantity = data.get('quantity')
        self.paid_status = data.get('paid_status')


@transaction_bp.post('/create')
@jwt_required()
def api_create_transaction(body: CreateTransactionBody):
    try:
        form = TransactionForm()

        transaction = TransactionService.create_transaction(
            form.user_id,
            form.product_id,
            form.quantity,
            form.voucher_id
        )
        return jsonify({
            'message': 'Transaction created successfully',
            'status': 201,
            'data': transaction.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({
            'message': str(e),
            'status': 400
        }), 400
    
@transaction_bp.get('/all')
@jwt_required()
def api_get_all_transactions():
    sort = request.args.get('sort')
    order = request.args.get('order', 'asc')

    transactions = TransactionService.get_all_transactions(sort, order)
    return jsonify({
        'status': 200,
        'data': transactions
    }) if transactions else ('', 404)

@transaction_bp.get('/<int:id>')
@jwt_required()
def api_get_transaction_by_id(path: TransactionPath):
    transaction = TransactionService.get_transaction_by_id(path.id)
    return jsonify({
        'status': 200,
        'data': transaction
    }) if transaction else ('', 404)

@transaction_bp.put('/<int:id>')
@jwt_required()
def api_update_transaction(path: TransactionPath, body: UpdateTransactionBody):
    try:
        form = TransactionForm()
        transaction = TransactionService.update_transaction(
            path.id,
            form.product_id,
            form.quantity,
            form.voucher_id,
            form.paid_status
        )
        return jsonify({
            'message': 'Transaction updated successfully',
            'status': 201,
            'data': transaction
        }), 201
    except NotFoundError as e:
        return jsonify({'error': {
            'message': str(e),
            'status': 404
        }}), 404
    except ValueError as e:
        return jsonify({
            'message': str(e),
            'status': 400
        }), 400