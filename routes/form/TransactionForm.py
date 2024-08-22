from pydantic import BaseModel


class BaseTransactionBody(BaseModel):
    user_id: int
    product_id: int
    voucher_id: int
    quantity: int


class TransactionPath(BaseModel):
    id: int
