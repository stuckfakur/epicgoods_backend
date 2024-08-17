from pydantic import BaseModel, Field, EmailStr


# create
class CreateBody(BaseModel):
    category_slug: str
    category_name: str
    description: str

class UpdateBody(BaseModel):
    category_name: str
    description: str

class CategoryPath(BaseModel):
    id: int
