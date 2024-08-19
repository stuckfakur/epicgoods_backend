from repositories.TransactionRepository import TransactionRepository
import re

class Validator:
    @staticmethod
    def transaction_validator(stock, price):
        if stock < 0:
            raise ValueError("Stock cannot be negative")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if not isinstance(stock, int):
            raise ValueError("Stock must be an integer")
        if not isinstance(price, int):
            raise ValueError("Price must be a integer")
    @staticmethod
    def paid_status_validator(paid_status):
        if not paid_status or not isinstance(paid_status, str):
            raise ValueError("paid_status must be a string")
    @staticmethod
    def user_id_validator(user_id):
        if not user_id or not isinstance(user_id, int):
            raise ValueError("user_id must be an integer")
    @staticmethod
    def product_id_validator(product_id):
        if not product_id or not isinstance(product_id, int):
            raise ValueError("product_id must be an integer")
    @staticmethod
    def voucher_id_validator(voucher_id):
        if not voucher_id or not isinstance(voucher_id, int):
            raise ValueError("voucher_id must be an integer")
    
class TransactionService:
    @staticmethod
    def create_transaction(
        user_id, 
        product_id, 
        voucher_id, 
        stock, 
        price, 
        paid_status
    ):
        Validator.transaction_validator(stock, price)
        Validator.paid_status_validator(paid_status)
        Validator.user_id_validator(user_id)
        Validator.product_id_validator(product_id)
        Validator.voucher_id_validator(voucher_id)
        transaction = TransactionRepository.create_transaction(
            user_id, 
            product_id, 
            voucher_id, 
            stock, 
            price, 
            paid_status
        )
        return transaction