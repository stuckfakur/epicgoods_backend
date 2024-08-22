from models.Transaction import Transaction, db
from repositories.ProductRepository import ProductRepository


class TransactionRepository:
    @staticmethod
    def create_transaction(
            user_id,
            product_id,
            voucher_id,
            quantity,
    ):
        new_transaction = Transaction(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity,
        )
        # if have voucher_id
        if voucher_id:
            new_transaction.voucher_id = voucher_id

        find_product = ProductRepository.get_product_by_id(product_id)
        new_transaction.total_price = quantity * find_product.product_price

        # paid status set to pending
        new_transaction.paid_status = 'pending'

        # update the product stock
        update_product_stock(product_id, quantity)

        db.session.add(new_transaction)
        db.session.commit()
        return new_transaction


@staticmethod
def update_product_stock(product_id, quantity):
    product = ProductRepository.get_product_by_id(product_id)
    product.product_stock -= quantity
    db.session.commit()
    return product
