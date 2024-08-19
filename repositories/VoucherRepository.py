from models.Voucher import Voucher, db

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
            voucher_name = voucher_name,
            voucher_code = voucher_code,
            voucher_type = voucher_type,
            voucher_value = voucher_value,
            voucher_quota = voucher_quota,
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