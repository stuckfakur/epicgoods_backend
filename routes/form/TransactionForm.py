from pydantic import BaseModel

class BaseTransactionBody(BaseModel):
    user_id: int
    product_id: int
    voucher_id: int
    quantity: int
    total_price: int
    paid_status: str

class TransactionPath(BaseModel):
    id: int
