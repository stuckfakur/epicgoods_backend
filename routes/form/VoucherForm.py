from pydantic import BaseModel

class CreateVoucherBody(BaseModel):
    voucher_name: str  
    voucher_code: str
    voucher_type: str
    voucher_value: int
    voucher_quota: int

class UpdateVoucherBody(BaseModel):
    voucher_name: str
    voucher_code: str
    voucher_type: str
    voucher_value: int
    voucher_quota: int

class VoucherPatch(BaseModel):
    id: int