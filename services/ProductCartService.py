from repositories.ProductCartRepository import ProductCartRepository
from utils.exception import NotFoundError
from sqlalchemy.exc import DataError

class Validator:
    @staticmethod
    def product_id_validator(product_id):
        if not product_id or not isinstance(product_id, int):
            raise ValueError("Product ID is required")
    
    @staticmethod
    def user_id_validator(user_id):
        if not user_id or not isinstance(user_id, int):
            raise ValueError("User ID is required")
        
    @staticmethod
    def product_cart_validator(quantity,):
        if not quantity or not isinstance(quantity, int):
            raise ValueError("Quantity is required")
        
class ProductCartService:
    @staticmethod
    def create_product_cart(user_id, product_id, quantity):
        Validator.user_id_validator(user_id)
        Validator.product_id_validator(product_id)
        Validator.product_cart_validator(quantity)
        product_cart = ProductCartRepository.create_product_cart(
            user_id,
            product_id,
            quantity
        )
        return product_cart
    
    @staticmethod
    def get_all_product_cart(sort=None, order='asc'):
        product_cart = ProductCartRepository.get_all_product_cart(sort, order)
        return [product_cart.to_dict() for product_cart in product_cart]
    
    @staticmethod
    def get_product_cart_by_id(productCartId):
        product_cart = ProductCartRepository.get_product_cart_by_id(productCartId)
        if product_cart:
            return product_cart.to_dict()
        else:
            return "Product cart not Found"
        
    @staticmethod
    def update_product_cart(
        productCartId,
        product_id,
        quantity
    ):
        Validator.product_id_validator(product_id)
        Validator.product_cart_validator(quantity)
        product_cart = ProductCartRepository.get_product_cart_by_id(productCartId)
        if not product_cart:
            raise NotFoundError("Product cart not found")
        try:
            product_cart = ProductCartRepository.update_product_cart(
                productCartId,
                product_id,
                quantity
            )
            return product_cart.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            raise e

    @staticmethod
    def update_product_cart_product_id(productCartId, product_id):
        data = ProductCartService.get_product_cart_by_id(productCartId)
        if not data:
            raise NotFoundError("Product cart not found")
        
        product_cart = ProductCartRepository.update_product_cart_product_id(productCartId, product_id)
        return product_cart
    
    @staticmethod
    def update_product_cart_quantity(productCartId, quantity):
        data = ProductCartService.get_product_cart_by_id(productCartId)
        if not data:
            raise NotFoundError("Product cart not found")
        
        product_cart = ProductCartRepository.update_product_cart_quantity(productCartId, quantity)
        return product_cart