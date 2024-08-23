from models.Transaction import Transaction, db
from repositories.ProductRepository import ProductRepository
from repositories.VoucherRepository import VoucherRepository
from sqlalchemy.exc import DataError

class TransactionRepository:
    @staticmethod
    def create_transaction(
            user_id,
            product_id,
            quantity,
            voucher_id
    ):
        new_transaction = Transaction(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity,
        )
        # if have voucher_id
        find_product = ProductRepository.get_product_by_id(product_id)

        # if quantity greater than stock
        if find_product.product_stock < new_transaction.quantity :
            raise ValueError("Not enough stock to complete this transaction") 
        
        elif voucher_id:
            new_transaction.voucher_id = voucher_id
            subtotal = quantity * find_product.product_price
            # value - amount of voucher
            new_transaction.total_price = calculate_total_price_with_voucher(subtotal, voucher_id)
        else:
            new_transaction.total_price = quantity * find_product.product_price

        # paid status set to pending
        new_transaction.paid_status = 'pending'

        # update the product stock
        update_pending_product_stock(product_id, quantity)

        db.session.add(new_transaction)
        db.session.commit()
        return new_transaction
    
    @staticmethod
    def get_all_transcations(sort=None, order='asc'):
        query = Transaction.query
        if sort:
            if order == 'desc':
                query = query.order_by(db.desc(getattr(Transaction, sort)))
            else:
                query = query.order_by(db.asc(getattr(Transaction, sort)))
        return query.all()

    @staticmethod
    def get_transaction_by_id(transactionId):
        return Transaction.query.get(transactionId)


    @staticmethod
    def update_transaction(
            transactionId,
            product_id,
            quantity,
            voucher_id,
            paid_status
    ):
        try:
            data = Transaction.query.get(transactionId)
            if not data:
                return None
            
            data.product_id=product_id
            data.quantity=quantity
            data.voucher_id=voucher_id
            data.paid_status=paid_status

            data.update_at=db.func.now()

            db.session.commit()
            return data
        except DataError as e:
            db.session.rollback()
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise e    
    
@staticmethod
def update_pending_product_stock(product_id, quantity):
    product = ProductRepository.get_product_by_id(product_id)
    product.product_stock -= quantity
    db.session.commit()
    return product

@staticmethod
def update_reject_product_stock(product_id, quantity):
    product = ProductRepository.get_product_by_id(product_id)
    product.product_stock += quantity
    db.session.commit()
    return product

@staticmethod
def calculate_total_price_with_voucher(subtotal, voucher_id):
    voucher = VoucherRepository.get_voucher_by_id(voucher_id)
    subtotal -= voucher.voucher_value
    return subtotal

@staticmethod
def process_paid_status(transaction_id):
    transaction = TransactionRepository.get_transaction_by_id(transaction_id)
    if not transaction:
        return 'Transaction not found', 404

    if transaction.paid_status == 'reject':
        update_reject_product_stock(transaction.product_id, transaction.quantity)
    elif transaction.paid_status == 'paid':
        db.session.commit()
        
    return 'Transaction Successful'
