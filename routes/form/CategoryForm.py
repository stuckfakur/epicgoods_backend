from pydantic import BaseModel, Field, EmailStr


# create
class CreateBody(BaseModel):
    category_slug: str
    category_name: str
    description: str

class UpdateBody(BaseModel):
    category_name: str
    description: str

class UpdateCategorySlugBody(BaseModel):
    category_slug: str

class UpdateCategoryNameBody(BaseModel):
    category_name: str

class UpdateCategoryDescriptionBody(BaseModel):
    description: str

class CategoryPath(BaseModel):
    id: int
