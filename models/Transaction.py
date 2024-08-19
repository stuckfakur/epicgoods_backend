from . import db

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    product_id = db.Column(db.ForeignKey('products.id'))
    voucher_id = db.Column(db.ForeignKey('vouchers.id'), nullable=True)
    stock = db.Column(db.Integer)
    price = db.Column(db.Integer)
    paid_status = db.Column(db.String(2))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    user = db.relationship('User', backref='transactions', lazy=True)
    product = db.relationship('Product', backref='transactions', lazy=True)
    voucher = db.relationship('Voucher', backref='transactions', lazy=True)
    def to_dict(self):
        return {
            'id' : self.id,
            'user_id' : self.user_id,
            'product_id' : self.product_id,
            'voucher_id' : self.voucher_id,
            'stock' : self.stock,
            'price' : self.price,
            'paid_status' : self.paid_status,
            'user' : {
                'id' : self.user.id,
                'name' : self.user.name,
            },
            'product' : {
                'id' : self.product.id,
                'name' : self.product.name,
                'price' : self.product.price,
                'stock' : self.product.stock,
            },
            'voucher' : {
                'id' : self.voucher.id,
                'name' : self.voucher.name,
                'discount' : self.voucher.discount,
            },
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }
    
    def repr(self) -> str:
        return f'<Transaction {self.id}>'