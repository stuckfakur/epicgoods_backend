from pydantic import BaseModel


class BaseCategoryModel(BaseModel):
    updated_at: str
    created_at: str


class CategoryDetailResponse(BaseCategoryModel):
    id: int
    category_slug: str
    category_photo: str
    category_name: str
    description: str


# create
class CreateBody(BaseModel):
    category_slug: str
    category_photo: str
    category_name: str
    description: str


class UpdateBody(BaseModel):
    category_name: str
    category_photo: str
    description: str


class UpdateCategorySlugBody(BaseModel):
    category_slug: str


class UpdateCategoryNameBody(BaseModel):
    category_name: str


class UpdateCategoryDescriptionBody(BaseModel):
    description: str


class CategoryPath(BaseModel):
    id: int
