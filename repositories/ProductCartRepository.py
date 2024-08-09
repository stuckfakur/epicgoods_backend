from models.ProductCart import ProductCart

class ProductCartRepository:
    @staticmethod
    def get_all_product_cart():
        return ProductCart.query.all()
    def get_product_cart_by_id(id):
        return ProductCart.query.get(id)
    def create_product_cart(
        user_id,
        product_id,
        quantity
    ):
        return ProductCart(
            user_id,
            product_id,
            quantity
        )
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