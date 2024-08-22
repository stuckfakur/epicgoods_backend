from enum import Enum

from . import db


class PaidStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    REJECT = "reject"


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    product_id = db.Column(db.ForeignKey('products.id'))
    voucher_id = db.Column(db.ForeignKey('vouchers.id'), nullable=True)
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    paid_status = db.Column(db.Enum(PaidStatus))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    user = db.relationship('User', backref='transactions', lazy=True)
    product = db.relationship('Product', backref='transactions', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'voucher_id': self.voucher_id,
            'quantity': self.quantity,
            'total_price': self.total_price,
            'paid_status': self.paid_status.value,
            'user': {
                'id': self.user.id,
                'name': self.user.name,
            },
            'product': {
                'id': self.product.id,
                'product_name': self.product.product_name,
                'product_price': self.product.product_price,
                'product_stock': self.product.product_stock,
            },
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def repr(self) -> str:
        return f'<Transaction {self.id}>'
