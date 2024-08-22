from repositories.TransactionRepository import TransactionRepository


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



class TransactionService:
    @staticmethod
    def create_transaction(
            user_id,
            product_id,
            voucher_id,
            quantity,
    ):
        Validator.transaction_validator(quantity, )
        Validator.user_id_validator(user_id)
        Validator.product_id_validator(product_id)
        return TransactionRepository.create_transaction(
            user_id,
            product_id,
            voucher_id,
            quantity,
        )
