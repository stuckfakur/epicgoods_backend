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

class UpdateVoucherName(BaseModel):
    voucher_name: str

class UpdateVoucherCode(BaseModel):
    voucher_code: str

class UpdateVoucherType(BaseModel):
    voucher_type: str

class UpdateVoucherValue(BaseModel):
    voucher_value: int

class UpdateVoucherQuota(BaseModel):
    voucher_quota: int

class VoucherPath(BaseModel):
    id: int