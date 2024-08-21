from models.ProductCart import ProductCart, db
from sqlalchemy.exc import DataError

class ProductCartRepository:
    @staticmethod
    def create_product_cart(
        user_id,
        product_id,
        quantity
    ):
        new_product_cart = ProductCart(
            user_id = user_id,
            product_id = product_id,
            quantity = quantity
        )
        db.session.add(new_product_cart)
        db.session.commit()
        return new_product_cart

    @staticmethod
    def get_all_product_cart(sort=None, order='asc'):
        query = ProductCart.query
        if sort:
            if order == 'desc':
                query = query.order_by(db.desc(getattr(ProductCart, sort)))
            else:
                query = query.order_by(db.asc(getattr(ProductCart, sort)))
        return query.all()
    
    @staticmethod
    def get_product_cart_by_id(id):
        return ProductCart.query.get(id)

    def update_product_cart(
        id,
        user_id,
        product_id,
        quantity
    ):
        return ProductCart.query.update(
            user_id,
            product_id,
            quantity
        )

    @staticmethod
    def update_product_cart(
        productCartId,
        product_id,
        quantity
    ):
        try:
            data = ProductCart.query.get(productCartId)
            if not data:
                return None
            
            data.product_id = product_id
            data.quantity = quantity
            data.updated_at = db.func.now()

            db.session.commit()
            return data

        except DataError as e:
            db.session.rollback()
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_product_cart_product_id(productCartId, product_id):
        try:
            product_cart = ProductCart.query.get(productCartId)
            if not product_cart:
                return None
            
            product_cart.product_id = product_id
            product_cart.updated_at = db.func.now()

            db.session.commit()
            return product_cart
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_product_cart_quantity(productCartId, quantity):
        try:
            product_cart = ProductCart.query.get(productCartId)
            if not product_cart:
                return None
            
            product_cart.quantity = quantity
            product_cart.updated_at = db.func.now()

            db.session.commit()
            return product_cart
        except Exception as e:
            db.session.rollback()
            raise e