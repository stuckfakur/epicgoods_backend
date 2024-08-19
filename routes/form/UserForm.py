from pydantic import BaseModel, Field

class CreateUserBody(BaseModel):
    name : str 
    email : str
    password : str

class UpdateUserBody(BaseModel):
    name : str
    email : str
    password : str

class UpdateUserStatusBody(BaseModel):
    status : str

class UpdateUserPasswordBody(BaseModel):
    password : str

class UpdateUserIsSellerBody(BaseModel):
    is_seller : str

class UserPath(BaseModel):
    id : int