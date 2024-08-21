from models.Transaction import Transaction, db

class TransactionRepository:
    @staticmethod
    def create_transaction(
        user_id, 
        product_id, 
        voucher_id, 
        quantity,
        total_price, 
        paid_status
    ):
        new_transaction = Transaction(
            user_id = user_id,
            product_id = product_id, 
            voucher_id = voucher_id, 
            quantity = quantity, 
            total_price = total_price, 
            paid_status = paid_status
        )
        db.session.add(new_transaction)
        db.session.commit()
        return new_transaction