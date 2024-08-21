from pydantic import BaseModel

class BaseProductCartBody(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class UpdateProductCartBody(BaseModel):
    product_id: int
    quantity: int

class UpdateProductIdBody(BaseModel):
    product_id: int

class UpdateProductQuantityBody(BaseModel):
    quantity: int

class ProductCartPath(BaseModel):
    id: int