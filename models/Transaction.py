from . import db

class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    product_id = db.Column(db.ForeignKey('products.id'))
    stock_id = db.Column(db.integer)
    price = db.Column(db.integer)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            'id' : self.id,
            'user_id' : self.user_id,
            'product_id' : self.product_id,
            'stock_id' : self.stock_id,
            'price' : self.price,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }
    
    def repr(self) -> str:
        return f'<Transaction {self.id}>'