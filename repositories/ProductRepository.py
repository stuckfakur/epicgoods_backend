from models.Product import Product, db

class ProductRepository:
    
    @staticmethod
    def get_all_product():
        return Product.query.all()
    
    @staticmethod
    def get_product_by_id(id):
        return Product.query.get(id)

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
       new_product = Product(
            product_photo = product_photo,
            product_gellery = product_gellery,
            product_name = product_name,
            product_price = product_price,
            product_stock = product_stock,
            product_condition = product_condition,
            product_detail = product_detail,
            status = status
       )
       db.session.add(new_product)
       db.session.commit()
       return new_product