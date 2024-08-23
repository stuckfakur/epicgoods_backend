from typing import List
from pydantic import BaseModel

class CreateTransactionBody(BaseModel):
    user_id: int
    product_id: int
    voucher_id: int
    quantity: int

class MakeManyTransactionBody(BaseModel):
    ListTransaction: List[CreateTransactionBody]


class UpdateTransactionBody(BaseModel):
    product_id: int
    quantity: int
    voucher_id: int
    paid_status: str
    
class TransactionPath(BaseModel):
    id: int