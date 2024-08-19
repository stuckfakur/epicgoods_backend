from pydantic import BaseModel

class CreateSellerBody(BaseModel):
    user_id: int
    location_id: int
    address: str
    store_name: str
    store_info: str
    description: str

class UpdateSellerBody(BaseModel):
    location_id: int
    address: str
    store_name: str
    store_info: str
    description: str

class UpdateSellerLocationIdBody(BaseModel):
    location_id: int

class UpdateSellerAddressBody(BaseModel):
    address: str

class UpdateSellerStoreNameBody(BaseModel):
    store_name: str

class UpdateSellerStoreTypeBody(BaseModel):
    store_type: str

class UpdateSellerStoreInfoBody(BaseModel):
    store_info: str

class UpdateSellerDescriptionBody(BaseModel):
    description: str

class SellerPath(BaseModel):
    id: int