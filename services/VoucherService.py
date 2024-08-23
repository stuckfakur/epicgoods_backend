from sqlalchemy.exc import DataError

from repositories.VoucherRepository import VoucherRepository
from utils.exception import NotFoundError


class Validator:
    @staticmethod
    def voucher_validator(voucher_name, voucher_code, voucher_value, voucher_quota):
        if not voucher_name or not isinstance(voucher_name, str):
            raise ValueError("Voucher name is required")
        if not voucher_code or not isinstance(voucher_code, str):
            raise ValueError("Voucher code is required")
        if not voucher_value or not isinstance(voucher_value, int):
            raise ValueError("Voucher value is required")
        if not voucher_quota or not isinstance(voucher_quota, int):
            raise ValueError("Voucher quota is required")

    # type only percentage or amount
    @staticmethod
    def voucher_type_validator(voucher_type):
        if voucher_type not in ['percentage', 'amount']:
            raise ValueError("Voucher type only percentage or amount")

    @staticmethod
    def exist_voucher(voucher_code):
        if VoucherRepository.existing_voucher_code(voucher_code):
            raise ValueError("Voucher code already exists")

class VoucherService:
    @staticmethod
    def create_voucher(
            voucher_name,
            voucher_code,
            voucher_type,
            voucher_value,
            voucher_quota
    ):
        Validator.voucher_validator(
            voucher_name,
            voucher_code,
            voucher_value,
            voucher_quota
        )
        Validator.voucher_type_validator(voucher_type)
        Validator.exist_voucher(voucher_code)
        return VoucherRepository.create_voucher(
            voucher_name,
            voucher_code,
            voucher_type,
            voucher_value,
            voucher_quota
        )

    @staticmethod
    def get_all_voucher(sort=None, order='asc'):
        voucher = VoucherRepository.get_all_voucher(sort, order)
        return [voucher.to_dict() for voucher in voucher]

    @staticmethod
    def get_voucher_by_id(voucherId):
        voucher = VoucherRepository.get_voucher_by_id(voucherId)
        if voucher:
            return voucher.to_dict()
        else:
            return "Voucher not Found"

    @staticmethod
    def update_voucher(
            voucherId,
            voucher_name,
            voucher_code,
            voucher_type,
            voucher_value,
            voucher_quota
    ):
        Validator.voucher_validator(
            voucher_name,
            voucher_code,
            voucher_value,
            voucher_quota
        )
        Validator.voucher_type_validator(voucher_type)
        Validator.exist_voucher(voucher_code)
        voucher = VoucherService.get_voucher_by_id(voucherId)
        if not voucher:
            raise NotFoundError("Voucher not found")
        try:
            voucher = VoucherRepository.update_voucher(
                voucherId,
                voucher_name,
                voucher_code,
                voucher_type,
                voucher_value,
                voucher_quota
            )
            return voucher.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            raise e
    
    @staticmethod
    def update_voucher_name(id, voucher_name):
        voucher = VoucherService.get_voucher_by_id(id)
        if not voucher:
            raise NotFoundError("Voucher not found")
        try:
            voucher = VoucherRepository.update_voucher_name(id, voucher_name)
            return voucher.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            raise e
    
    @staticmethod
    def update_voucher_code(id,voucher_code):
        voucher = VoucherService.get_voucher_by_id(id)
        if not voucher:
            raise NotFoundError("Voucher not found")
        try:
            voucher = VoucherRepository.update_voucher_code(id, voucher_code)
            return voucher.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            raise e
    
    @staticmethod
    def update_voucher_type(id, voucher_type):
        Validator.voucher_type_validator(voucher_type)
        voucher = VoucherService.get_voucher_by_id(id)
        if not voucher:
            raise NotFoundError("Voucher not found")
        try:
            voucher = VoucherRepository.update_voucher_type(id, voucher_type)
            return voucher.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            raise e
        
    @staticmethod
    def update_voucher_value(id, voucher_value):
        voucher = VoucherService.get_voucher_by_id(id)
        if not voucher:
            raise NotFoundError("Voucher not found")
        try:
            voucher = VoucherRepository.update_voucher_value(id, voucher_value)
            return voucher.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            raise e
        
    @staticmethod
    def update_voucher_quota(id, voucher_quota):
        voucher = VoucherService.get_voucher_by_id(id)
        if not voucher:
            raise NotFoundError("Voucher not found")
        try:
            voucher = VoucherRepository.update_voucher_quota(id, voucher_quota)
            return voucher.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            raise e

    @staticmethod
    def delete_voucher(productId):
        data = VoucherRepository.get_voucher_by_id(productId)
        if not data:
            raise NotFoundError("Voucher not found")
        voucher = VoucherRepository.delete_voucher(productId)
        return voucher.to_dict()