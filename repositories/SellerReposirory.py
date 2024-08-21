from models.Seller import Seller, db
from sqlalchemy.exc import DataError

class SellerRepository:
    @staticmethod
    def create_seller(
        user_id,
        location_id,
        address,
        store_name,
        store_info,
        description,
    ):
       new_seller = Seller(
           user_id = user_id,
           location_id = location_id,
           address = address,
           store_name = store_name,
           store_info = store_info,
           description = description,
       )
       db.session.add(new_seller)
       db.session.commit()
       return new_seller
    
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
    def existing_store_name(store_name, user_id=None):
        existing = Seller.query.filter_by(store_name=store_name)
        if user_id:
            existing = existing.filter(Seller.id != user_id)

        existing = existing.first()
        return True if existing else False
    
    @staticmethod
    def update_seller(
        id, 
        location_id, 
        address, 
        store_name, 
        store_type, 
        store_info, 
        description
    ):
        try:
            data = Seller.query.get(id)
            if not data:
                return None

            # Update the seller fields
            data.location_id = location_id
            data.address = address
            data.store_type = store_type
            data.store_info = store_info
            data.description = description
            data.updated_at = db.func.now()

            if store_name and store_name != data.store_name:
                if SellerRepository.existing_store_name(store_name, id):
                    raise ValueError('Store name already exists')
                data.store_name = store_name

            db.session.commit()
            return data

        except DataError as e:
            db.session.rollback()
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_seller_location_id(sellerId, location_id):
        try:
            seller = Seller.query.get(sellerId)
            if not seller:
                return None
            
            seller.location_id = location_id
            seller.updated_at = db.func.now()

            db.session.commit()
            return seller
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_seller_address(sellerId, address):
        try:
            seller = Seller.query.get(sellerId)
            if not seller:
                return None
            
            seller.address = address
            seller.updated_at = db.func.now()

            db.session.commit()
            return seller
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_seller_store_name(sellerId, store_name):
        try:
            seller = Seller.query.get(sellerId)
            if not seller:
                return None
            
            seller.store_name = store_name
            seller.updated_at = db.func.now()

            db.session.commit()
            return seller
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def update_seller_store_type(sellerId, store_type):
        try:
            seller = Seller.query.get(sellerId)
            if not seller:
                return None
            
            seller.store_type = store_type
            seller.updated_at = db.func.now()

            db.session.commit()
            return seller
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_seller_store_info(sellerId, store_info):
        try:
            seller = Seller.query.get(sellerId)
            if not seller:
                return None
            
            seller.store_info = store_info
            seller.updated_at = db.func.now()

            db.session.commit()
            return seller
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_seller_description(sellerId, description):
        try:
            seller = Seller.query.get(sellerId)
            if not seller:
                return None
            
            seller.description = description
            seller.updated_at = db.func.now()

            db.session.commit()
            return seller
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_seller(id):
        seller = Seller.query.get(id)
        if seller:
            db.session.delete(seller)
            db.session.commit()
        return seller


