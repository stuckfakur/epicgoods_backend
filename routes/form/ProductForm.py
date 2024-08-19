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
    product_gallery: object
    product_name: str
    product_price: int
    product_stock: int
    product_condition: str
    product_detail: str
    status: str
    category_id: int

class UpdateProductCategoryIdBody(BaseModel):
    category_id: int

class UpdateProductSlugBody(BaseModel):
    product_slug: str

class UpdateProductPhotoBody(BaseModel):
    product_photo: str

class UpdateProductGalleryBody(BaseModel):
    product_gallery: object

class UpdateProductNameBody(BaseModel):
    product_name: str

class UpdateProductPriceBody(BaseModel):
    product_price: int

class UpdateProductStockBody(BaseModel):
    product_stock: int

class UpdateProductConditionBody(BaseModel):
    product_condition: str

class UpdateProductDetailBody(BaseModel):
    product_detail: str

class UpdateProductStatusBody(BaseModel):
    status: str

class ProductPath(BaseModel):
    id: int