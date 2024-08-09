from repositories.ProductRepository import ProductRepository

class ProductService:
    @staticmethod
    def get_all_product():
        product = ProductRepository.get_all_product()
        return [product.to_dict() for product in product]
    
    @staticmethod
    def get_product_by_id(id):
        return ProductRepository.get_product_by_id(id)

    @staticmethod
    def create_product(
        product_photo,
        product_gellery,
        product_name,
        product_price,
        product_stock,
        product_condition,
        product_detail,
        status
    ):
        return ProductRepository.create_product(
        product_photo,
        product_gellery,
        product_name,
        product_price,
        product_stock,
        product_condition,
        product_detail,
        status
        )