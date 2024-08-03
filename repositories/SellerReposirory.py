from models.Seller import Seller, db

class SellerRepository:
    
    @staticmethod
    def get_all_seller():
        return Seller.query.all()
    
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