from . import db
from flask_login import UserMixin

class ProductCart(UserMixin, db.Model):
    __tablename__ = 'product_carts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    product_id = db.Column(db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


    user = db.relationship('User', backref='product_carts', lazy=True)
    product = db.relationship('Product', backref='product_carts', lazy=True)
    def to_dict(self):
        return{
            'id' : self.id,
            'user_id': self.user_id,
            'product_id' : self.product_id,
            'quantity' : self.quantity,
            'user' : {
                'id' : self.user.id,
                'name' : self.user.name
            },
            'product' : {
                'id' : self.product.id,
                'product_name' : self.product.product_name,
                'product_price' : self.product.product_price,
                'product_stock' : self.product.product_stock

            },
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }
    
    def __repr__(self) -> str:
        return f"<ProductCart {self.id}>"