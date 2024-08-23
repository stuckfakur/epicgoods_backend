from repositories.TransactionRepository import TransactionRepository
from utils.exception import NotFoundError 
from sqlalchemy.exc import DataError

class Validator:
    @staticmethod
    def transaction_validator(quantity):
        if quantity < 0:
            raise ValueError("Stock cannot be negative")
        if not isinstance(quantity, int):
            raise ValueError("Stock must be an integer")

    @staticmethod
    def user_id_validator(user_id):
        if not user_id or not isinstance(user_id, int):
            raise ValueError("user_id must be an integer")

    @staticmethod
    def product_id_validator(product_id):
        if not product_id or not isinstance(product_id, int):
            raise ValueError("product_id must be an integer")
        
    @staticmethod
    def paid_status_validator(paid_status):
        if paid_status not in ['pending', 'paid','reject']:
            raise ValueError("Paid status must be 'pending', 'paid' or 'reject'")

class TransactionService:
    @staticmethod
    def create_transaction(
            user_id,
            product_id,
            voucher_id,
            quantity,
    ):
        Validator.transaction_validator(quantity)
        Validator.user_id_validator(user_id)
        Validator.product_id_validator(product_id)
        return TransactionRepository.create_transaction(
            user_id,
            product_id,
            voucher_id,
            quantity,
        )
    
    @staticmethod
    def get_all_transactions(sort=None, order='asc'):
        transaction = TransactionRepository.get_all_transcations(sort, order)
        return [transaction.to_dict() for transaction in transaction]

    @staticmethod
    def get_transaction_by_id(transactionId):
        transaction = TransactionRepository.get_transaction_by_id(transactionId)
        if transaction:
            return transaction.to_dict()
        else:
            return "Transaction not Found"
        
    @staticmethod
    def update_transaction(
            transactionId,
            product_id,
            voucher_id,
            quantity,
            paid_status,
    ):
        Validator.transaction_validator(quantity)
        Validator.product_id_validator(product_id)
        Validator.paid_status_validator(paid_status)
        transaction = TransactionService.get_transaction_by_id(transactionId)
        if not transaction:
            raise NotFoundError("Transaction not found")
        try:
            transaction = TransactionRepository.update_transaction(
                transactionId,
                product_id,
                voucher_id,
                quantity,
                paid_status
            )
            return transaction.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            raise e