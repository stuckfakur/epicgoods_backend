from repositories.ProductRepository import ProductRepository
from utils.exception import NotFoundError

class Validator:
    @staticmethod
    def product_validator(product_slug, product_name, product_price, product_stock, product_condition, product_detail, status, user_id, category_id):
        if not product_slug or not isinstance(product_slug, str):
            raise ValueError("Product slug is required")
        if not product_name or not isinstance(product_name, str):
            raise ValueError("Product name is required")
        if not product_price or not isinstance(product_price, int):
            raise ValueError("Product price is required")
        if not product_stock or not isinstance(product_stock, int):
            raise ValueError("Product stock is required") 
        if not product_condition or not isinstance(product_condition, str):
            raise ValueError("Product condition is required")
        if not product_detail or not isinstance(product_detail, str):
            raise ValueError("Product detail is required")
        if not status or not isinstance(status, str):
            raise ValueError("Status is required")
        if not user_id or not isinstance(user_id, int):
            raise ValueError("User id is required")
        if not category_id or not isinstance(category_id, int):
            raise ValueError("Category id is required")
        
    @staticmethod
    def not_negative_price(product_price):
        if product_price < 0:
            raise ValueError("Product price cannot be negative")
        
class ProductService:
    @staticmethod
    def create_products(
        product_slug:object,
        product_photo:object,
        product_gellery:object,
        product_name:object ,
        product_price:object,
        product_stock:object,
        product_condition:object,
        product_detail:object,
        status:object,
        user_id:object,
        category_id:object

    ) -> object:
        Validator.product_validator(
            product_slug,
            product_name, 
            product_price, 
            product_stock, 
            product_condition, 
            product_detail, 
            status,
            user_id,
            category_id
        )
        Validator.not_negative_price(product_price)
        product = ProductRepository.api_create_products(
            product_slug,
            product_photo,
            product_gellery,
            product_name,
            product_price,
            product_stock,
            product_condition,
            product_detail,
            status,
            user_id,
            category_id
        )
        return product

    @staticmethod
    def get_all_products(sort:None, order='asc'):
        product = ProductRepository.api_get_all_products(sort, order)
        return [product.to_dict() for product in product]
    
    @staticmethod
    def get_product_by_id(id):
        product = ProductRepository.get_product_by_id(id)
        if not product:
            raise NotFoundError("Product not found")
        return product.to_dict()

    @staticmethod
    def delete_product(id):
        data = ProductRepository.get_product_by_id(id)
        if not data:
            raise NotFoundError("Product not found")
        product = ProductRepository.delete_product(id)
        return product