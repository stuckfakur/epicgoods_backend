from . import db


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_id = db.Column(db.ForeignKey('sellers.id'))
    category_id = db.Column(db.ForeignKey('categories.id'))
    product_slug = db.Column(db.String(80), unique=True, nullable=False)
    product_photo = db.Column(db.String(80))
    product_gallery = db.Column(db.Text)
    product_name = db.Column(db.String(80))
    product_price = db.Column(db.Integer)
    product_price_discount = db.Column(db.Integer)
    product_stock = db.Column(db.Integer)
    product_condition = db.Column(db.String(2))
    product_detail = db.Column(db.String(1000))
    is_discount = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(2))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    category = db.relationship('Category', backref='products', lazy=True)
    seller = db.relationship('Seller', backref='products', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'product_slug': self.product_slug,
            'product_photo': self.product_photo,
            'product_gallery': self.product_gallery,
            'product_name': self.product_name,
            'product_price': self.product_price,
            'product_price_discount': self.product_price_discount,
            'product_stock': self.product_stock,
            'product_condition': self.product_condition,
            'product_detail': self.product_detail,
            'is_discount': self.is_discount,
            'status': self.status,
            'category': {
                'id': self.category.id,
                'category_slug': self.category.category_slug,
                'category_name': self.category.category_name,
                'description': self.category.description
            },
            'seller': {
                'id': self.seller.id,
                'store_name': self.seller.store_name
            },
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self) -> str:
        return f"<Product {self.product_name}>"
