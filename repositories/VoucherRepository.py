from models.Voucher import Voucher, db
from sqlalchemy.exc import DataError

class VoucherRepository:
    @staticmethod
    def create_voucher(
            voucher_name,
            voucher_code,
            voucher_type,
            voucher_value,
            voucher_quota,
    ):
        new_voucher = Voucher(
            voucher_name=voucher_name,
            voucher_code=voucher_code,
            voucher_type=voucher_type,
            voucher_value=voucher_value,
            voucher_quota=voucher_quota,
        )
        db.session.add(new_voucher)
        db.session.commit()
        return new_voucher

    @staticmethod
    def existing_voucher_code(voucher_code, voucher_id=None):
        existing = Voucher.query.filter_by(voucher_code=voucher_code)
        if voucher_id:
            existing = existing.filter(Voucher.id != voucher_id)

        existing = existing.first()
        return True if existing else False

    @staticmethod
    def get_all_voucher(sort=None, order='asc'):
        query = Voucher.query
        if sort:
            if order == 'desc':
                query = query.order_by(db.desc(getattr(Voucher, sort)))
            else:
                query = query.order_by(db.asc(getattr(Voucher, sort)))
        return query.all()

    @staticmethod
    def get_voucher_by_id(voucherId):
        return Voucher.query.get(voucherId)

    @staticmethod
    def update_voucher(
            voucherId,
            voucher_name,
            voucher_code,
            voucher_type,
            voucher_value,
            voucher_quota
    ):
        try:
            voucher = Voucher.query.get(voucherId)
            if not voucher:
                return None
            voucher.voucher_name = voucher_name
            voucher.voucher_code = voucher_code
            voucher.voucher_type = voucher_type
            voucher.voucher_value = voucher_value
            voucher.voucher_quota = voucher_quota

            voucher.updated_at = db.func.now()

            db.session.commit()
            return voucher
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def update_voucher_name(voucherId, voucher_name):
        try:
            voucher = Voucher.query.get(voucherId)
            if not voucher:
                return None
            
            voucher.voucher_name = voucher_name
            voucher.updated_at = db.func.now()
            
            db.session.commit()
            return voucher
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def update_voucher_code(voucherId, voucher_code):
        try:
            voucher = Voucher.query.get(voucherId)
            if not voucher:
                return None
            
            voucher.voucher_code = voucher_code
            voucher.updated_at = db.func.now()
            
            db.session.commit()
            return voucher
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def update_voucher_type(voucherId, voucher_type):
        try:
            voucher = Voucher.query.get(voucherId)
            if not voucher:
                return None
            
            voucher.voucher_type = voucher_type
            voucher.updated_at = db.func.now()
            
            db.session.commit()
            return voucher
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_voucher_value(voucherId, voucher_value):
        try:
            voucher = Voucher.query.get(voucherId)
            if not voucher:
                return None
            
            voucher.voucher_value = voucher_value
            voucher.updated_at = db.func.now()
            
            db.session.commit()
            return voucher
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_voucher_quota(voucherId, voucher_quota):
        try:
            voucher = Voucher.query.get(voucherId)
            if not voucher:
                return None
            
            voucher.voucher_quota = voucher_quota
            voucher.updated_at = db.func.now()
            
            db.session.commit()
            return voucher
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_voucher(voucherId):
        voucher = Voucher.query.get(voucherId)
        if voucher:
            db.session.delete(voucher)
            db.session.commit()
        return voucher
