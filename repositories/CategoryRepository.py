from models.Category import Category, db

class CategoryRepository:
    @staticmethod
    def create_category(
        category_slug,
        category_name,
        category_photo,
        description
    ):
       new_category = Category(
           category_slug = category_slug,
           category_name = category_name,
           category_photo = category_photo,
           description = description
       )
       db.session.add(new_category)
       db.session.commit()
       return new_category

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
    def update_category(
            id, 
            category_slug,
            category_name,
            category_photo,
            description,
    ):
        try:
            data = Category.query.get(id)
            if not data:
                return None

            data.category_name = category_name
            data.category_slug = category_slug
            data.category_photo = category_photo
            data.description = description
            data.updated_at = db.func.now()

            db.session.commit()
            return data

        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_category_slug(id, category_slug):
        try:
            category = Category.query.get(id)
            if not category:
                return None

            category.category_slug = category_slug
            category.updated_at = db.func.now()

            db.session.commit()

            return category
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def update_category_name(id, category_name):
        try:
            category = Category.query.get(id)
            if not category:
                return None

            category.category_name = category_name
            category.updated_at = db.func.now()

            db.session.commit()

            return category
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def update_category_description(id, description):
        try:
            category = Category.query.get(id)
            if not category:
                return None

            category.description = description
            category.updated_at = db.func.now()

            db.session.commit()
            return category
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def delete_category(id):
        category = Category.query.get(id)
        if category:
            db.session.delete(category)
            db.session.commit()
        return category

 