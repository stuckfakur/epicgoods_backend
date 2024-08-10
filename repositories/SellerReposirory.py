from models.Seller import Seller, db

class SellerRepository:
    
    @staticmethod
    def get_all_seller(sort=None, order='asc'):
        query = Seller.query
        if sort:
            if order == 'desc':
                query = query.order_by(db.desc(getattr(Seller, sort)))
            else:
                query = query.order_by(db.asc(getattr(Seller, sort)))
        return query.all()
    
    @staticmethod
    def get_seller_by_id(id):
        return Seller.query.get(id)

    @staticmethod
    def create_seller(
        store_name,
        store_info,
        description
    ):
       new_seller = Seller(
           store_name = store_name,
           store_info = store_info,
           description = description
       )
       db.session.add(new_seller)
       db.session.commit()
       return new_seller
    
    @staticmethod
    def update_seller(id, data):
        seller = Seller.query.get(id)
        if seller:
            for key, value in data.items():
                setattr(seller, key, value)
            db.session.commit()
        return seller
    
    @staticmethod
    def delete_seller(id):
        seller = Seller.query.get(id)
        if seller:
            db.session.delete(seller)
            db.session.commit()
        return seller


