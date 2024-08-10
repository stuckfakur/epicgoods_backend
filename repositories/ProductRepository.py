from models.Product import Product, db

class ProductRepository:
    @staticmethod
    def api_create_products(
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

    ):
       new_product = Product(
            product_slug = product_slug,
            product_photo = product_photo,
            product_gellery = product_gellery,
            product_name = product_name,
            product_price = product_price,
            product_stock = product_stock,
            product_condition = product_condition,
            product_detail = product_detail,
            status = status,
            user_id = user_id,
            category_id = category_id
       )
       db.session.add(new_product)
       db.session.commit()
       return new_product

    @staticmethod
    def api_get_all_products(sort:None, order='asc'):
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
    def delete_product(id):
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product

