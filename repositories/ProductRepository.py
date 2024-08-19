from sqlalchemy.exc import DataError
from models.Product import Product, db


class ProductRepository:
    @staticmethod
    def api_create_products(
            product_slug,
            product_photo,
            product_gallery,
            product_name,
            product_price,
            product_stock,
            product_condition,
            product_detail,
            status,
            seller_id,
            category_id

    ):
        new_product = Product(
            product_slug=product_slug,
            product_photo=product_photo,
            product_gallery=product_gallery,
            product_name=product_name,
            product_price=product_price,
            product_stock=product_stock,
            product_condition=product_condition,
            product_detail=product_detail,
            status=status,
            seller_id=seller_id,
            category_id=category_id
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def api_get_all_products(sort: None, order='asc'):
        query = Product.query
        if sort:
            if order == 'desc':
                query = query.order_by(db.desc(getattr(Product, sort)))
            else:
                query = query.order_by(db.asc(getattr(Product, sort)))

        return query.all()

    @staticmethod
    def get_product_by_id(id):
        return Product.query.get(id)

    @staticmethod
    def update_product(
            productId,
            product_slug,
            product_photo,
            product_gallery,
            product_name,
            product_price,
            product_stock,
            product_condition,
            product_detail,
            status,
            category_id
    ):
        try:
            data = Product.query.get(productId)
            if not data:
                return None
            data.product_slug = product_slug
            data.product_photo = product_photo
            data.product_gallery = product_gallery
            data.product_name = product_name
            data.product_price = product_price
            data.product_stock = product_stock
            data.product_condition = product_condition
            data.product_detail = product_detail
            data.status = status
            data.category_id = category_id
            
            data.updated_at = db.func.now()

            db.session.commit()
            return data

        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_product_category(id, category_id):
        try:
            product = Product.query.get(id)
            if not product:
                raise None
            product.category_id = category_id
            product.updated_at = db.func.now()
            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_product_slug(id, product_slug):
        try:
            product = Product.query.get(id)
            if not product:
                raise None
            product.product_slug = product_slug
            product.updated_at = db.func.now()
            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_product_photo(id, product_photo):
        try:
            product = Product.query.get(id)
            if not product:
                raise None
            product.product_photo = product_photo
            product.updated_at = db.func.now()
            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_product_gallery(id, product_gallery):
        try:
            product = Product.query.get(id)
            if not product:
                raise None
            product.product_gallery = product_gallery
            product.updated_at = db.func.now()
            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_product_name(sellerId, product_name):
        try:
            product = Product.query.get(sellerId)
            if not product:
                raise None
        
            product.product_name = product_name
            product.updated_at = db.func.now()
        
            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_product_price(id, product_price):
        try:
            product = Product.query.get(id)
            if not product:
                raise None
            product.product_price = product_price
            product.updated_at = db.func.now()
            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_product_stock(id, product_stock):
        try:
            product = Product.query.get(id)
            if not product:
                raise None
            product.product_stock = product_stock
            product.updated_at = db.func.now()
            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def update_product_condition(id, product_condition):
        try:
            product = Product.query.get(id)
            if not product:
                raise None
            product.product_condition = product_condition
            product.updated_at = db.func.now()
            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_product_detail(id, product_detail):
        try:
            product = Product.query.get(id)
            if not product:
                raise None
            product.product_detail = product_detail
            product.updated_at = db.func.now()
            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_product_status(id, status):
        try:
            product = Product.query.get(id)
            if not product:
                raise None
            product.status = status
            product.updated_at = db.func.now()
            db.session.commit()
            return product
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_product(id):
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product