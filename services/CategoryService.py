from repositories.CategoryRepository import CategoryRepository
from utils.exception import NotFoundError

class Validator:
    @staticmethod
    def category_validator(category_slug, category_name, description):
        if not category_slug or not isinstance(category_slug, str):
            raise ValueError("Category slug is required")
        if not category_name or not isinstance(category_name, str):
            raise ValueError("Category name is required")
        if not description or not isinstance(description, str):
            raise ValueError("Description is required")

class CategoryService:
    @staticmethod
    def create_category(category_slug: object, category_name: object, description: object) -> object:
        Validator.category_validator(category_slug, category_name, description)
        category = CategoryRepository.create_category(
            category_slug,
            category_name,
            description
        )
        return category

    @staticmethod
    def get_all_category(sort=None, order='asc'):
        category = CategoryRepository.get_all_category(sort, order)
        return [category.to_dict() for category in category]
    
    @staticmethod
    def get_category_by_id(id):
        category = CategoryRepository.get_category_by_id(id)
        if not category:
            raise NotFoundError("Category not found")
        return category.to_dict()
    
    @staticmethod
    def update_category(id: object, category_slug: object, category_name: object, description: object) -> object:
        Validator.category_validator(category_slug, category_name, description)
        category = CategoryRepository.get_category_by_id(id)
        if not category:
            raise NotFoundError("Category not found")
        try:
            category = CategoryRepository.update_category(
                id,
                category_slug,
                category_name,
                description
            )
            return category
        except Exception as e:
            raise e

    @staticmethod
    def delete_category(id):
        data = CategoryRepository.get_category_by_id(id)
        if not data:
            raise NotFoundError("Category not found")
        category = CategoryRepository.delete_category(id)
            
        return category




