from . import db
from flask_login import UserMixin

class Product(UserMixin, db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.ForeignKey('categories'))
    product_slug = db.Column(db.String(80), unique=True)
    product_photo = db.Column(db.String(80))
    product_gellery = db.Column(db.Text)
    product_name = db.Column(db.String(80))
    product_price = db.Column(db.Integer)
    product_stock = db.Column(db.Integer)
    product_condition = db.Column(db.String(2))
    product_detail = db.Column(db.String(1000))
    status = db.Column(db.String(2))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def to_dict(self):
        return{
            'id' : self.id,
            'category_id': self.category_id,
            'product_slug' : self.product_slug,
            'product_photo' : self.product_photo,
            'product_gellery' : self.product_gellery,
            'product_name' : self.product_name,
            'product_price' : self.product_price,
            'product_stock' : self.product_stock,
            'product_condition' : self.product_condition,
            'product_detail' : self.product_detail,
            'status' : self.status,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }
    
    

    def __repr__(self) -> str:
        return f"<Product {self.product_name}>"