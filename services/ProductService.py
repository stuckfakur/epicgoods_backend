from repositories.ProductRepository import ProductRepository
from utils.exception import NotFoundError
from sqlalchemy.exc import DataError
import re

class Validator:
    @staticmethod
    def product_validator(
        product_slug, 
        product_name, 
        product_price, 
        product_stock, 
        product_condition, 
        product_detail
    ):
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
        
        # regex_product_name = '^[a-zA-Z0-9]*$'
        # if not re.match(regex_product_name, product_name):
            # raise ValueError("Product name cannot contain special characters")

    @staticmethod
    def extra_validator(category_id):
        if not category_id or not isinstance(category_id, int):
            raise ValueError("Category id is required")

    @staticmethod
    def seller_validator(seller_id):
        if not seller_id or not isinstance(seller_id, int):
            raise ValueError("Seller id is required")

    @staticmethod
    def status_validator(status):
        if not status or not isinstance(status, str):
            raise ValueError("Status is required")

    @staticmethod
    def not_negative_price(product_price):
        if product_price < 0:
            raise ValueError("Product price cannot be negative")
        
class ProductService:
    @staticmethod
    def create_products(
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
        Validator.product_validator(
            product_slug,
            product_name, 
            product_price, 
            product_stock, 
            product_condition, 
            product_detail
        )
        Validator.extra_validator(category_id)
        Validator.seller_validator(seller_id)
        Validator.not_negative_price(product_price)
        product = ProductRepository.api_create_products(
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
    def update_product(
        id, 
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
        Validator.product_validator(
            product_slug,
            product_name, 
            product_price, 
            product_stock, 
            product_condition, 
            product_detail
        )
        Validator.extra_validator(category_id)
        Validator.seller_validator(seller_id)
        Validator.status_validator(status)
        Validator.not_negative_price(product_price)
        product = ProductRepository.get_product_by_id(id)
        if not product:
            raise NotFoundError("Product not found")
        try:
            product = ProductRepository.update_product(
                id, 
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
            )
            return product
        except DataError as e:
            raise e
        except Exception as e:
            raise e
        
    @staticmethod
    def delete_product(id):
        data = ProductRepository.get_product_by_id(id)
        if not data:
            raise NotFoundError("Product not found")
        product = ProductRepository.delete_product(id)
        return product