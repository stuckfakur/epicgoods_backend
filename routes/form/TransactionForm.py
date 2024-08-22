from typing import List
from pydantic import BaseModel

class CreateTransactionBody(BaseModel):
    user_id: int
    product_id: int
    voucher_id: int
    quantity: int

class MakeManyTransactionBody(BaseModel):
    ListTransaction: List[CreateTransactionBody]


class TransactionPath(BaseModel):
    id: int
