from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_openapi3 import APIBlueprint, Tag

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
