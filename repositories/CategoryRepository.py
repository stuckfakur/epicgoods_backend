from models.Category import Category, db

class CategoryRepository:
    
    @staticmethod
    def get_all_category():
        return Category.query.all()
    
    @staticmethod
    def get_category_by_id(id):
        return Category.query.get(id)

    @staticmethod
    def create_category(
        category_name,
        description
    ):
       new_category = Category(
           category_name = category_name,
           description = description
       )
       db.session.add(new_category)
       db.session.commit()
       return new_category