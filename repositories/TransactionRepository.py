from models.Transaction import Transaction, db

class TransactionRepository:
    @staticmethod
    def create_transaction(
        user_id, 
        product_id, 
        voucher_id, 
        stock, price, 
        paid_status
    ):
        transaction = Transaction(
            user_id, 
            product_id, 
            voucher_id, 
            stock, 
            price, 
            paid_status
        )
        db.session.add(transaction)
        db.session.commit()
        return transaction