from pydantic import BaseModel

class CreateProductBody(BaseModel):
    product_slug: str
    product_photo: str
    product_gallery: object
    product_name: str
    product_price: int
    product_stock: int
    product_condition: str
    product_detail: str
    status: str
    seller_id: int
    category_id: int

class UpdateProductBody(BaseModel):
    product_slug: str
    product_photo: str
    product_gallery: str
    product_name: str
    product_price: int
    product_stock: int
    product_condition: str
    product_detail: str
    status: str
    category_id: int

class ProductPath(BaseModel):
    id: int




