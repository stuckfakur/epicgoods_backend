from models.Category import Category, db

class CategoryRepository:
    
    @staticmethod
    def get_all_category(sort=None, order='asc'):
        query = Category.query
        if sort:
            if order == 'desc':
                query = query.order_by(db.desc(getattr(Category, sort)))
            else:
                query = query.order_by(db.asc(getattr(Category, sort)))

        return query.all()
    
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
    
    @staticmethod
    def update_category(
            id,
            category_name,
            description,
    ):
        try:
            data = Category.query.get(id)
            if not data:
                return None

            data.category_name = category_name
            data.description = description
            data.updated_at = db.func.now()

            db.session.commit()
            return data

        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def delete_category(id):
        category = Category.query.get(id)
        if category:
            db.session.delete(category)
            db.session.commit()
        return category

 