from repositories.CategoryRepository import CategoryRepository

class CategoryService:
    @staticmethod
    def get_all_category():
        category = CategoryRepository.get_all_category()
        return [category.to_dict() for category in category]
    
    @staticmethod
    def get_category_by_id(id):
        return CategoryRepository.get_category_by_id(id)

    @staticmethod
    def create_category(
        category_name,
        description
    ):
        return CategoryRepository.create_category(
            category_name,
            description
        )