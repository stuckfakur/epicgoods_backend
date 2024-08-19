from utils.exception import NotFoundError
from repositories.VoucherRepository import VoucherRepository
import re

class Validator:
    @staticmethod
    def voucher_validator(voucher_name, voucher_code, voucher_value, voucher_quota):
        if not voucher_name or not isinstance(voucher_name, str):
            raise NotFoundError("Voucher name is required")
        if not voucher_code or not isinstance(voucher_code, str):
            raise NotFoundError("Voucher code is required")
        if not voucher_value or not isinstance(voucher_value, int):
            raise NotFoundError("Voucher value is required")
        if not voucher_quota or not isinstance(voucher_quota, int):
            raise NotFoundError("Voucher quota is required")
        
        regex_voucher_code = '^[A-Za-z0-9]+$'
        if not re.match(regex_voucher_code,  voucher_code):
            raise NotFoundError("Voucher code is invalid")
    
    @staticmethod
    def voucher_type_validator(voucher_type):
        if not voucher_type or not isinstance(voucher_type, str):
            raise NotFoundError("Voucher type is required")

    @staticmethod
    def exist_voucher(voucher_code):
        if VoucherRepository.exist_voucher(voucher_code):
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
        Validator.voucher_type_validator(voucher_type)
        Validator.voucher_validator(
            voucher_name, 
            voucher_code, 
            voucher_value, 
            voucher_quota
        )
        Validator.exist_voucher(voucher_code)
        voucher = VoucherRepository.create_voucher(
            voucher_name, 
            voucher_code, 
            voucher_type, 
            voucher_value, 
            voucher_quota
        )
        return voucher






    




