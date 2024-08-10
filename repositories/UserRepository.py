from models.User import User, db

class UserRepository:

    @staticmethod
    def create_users(
        name,
        username,
        email,
        password,
        consumer_data
    ):
       new_user = User(
           name = name,
           username = username,
           email = email,
           consumer_data = consumer_data
       )
       new_user.set_password(password)
       db.session.add(new_user)
       db.session.commit()
       return new_user

    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def get_users_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def get_mydata_users(id):
        return User.query.get(id)

    @staticmethod
    def update_users(
        id,
        name,
        password=None,
    ):
        try:
            data = User.query.get(id)
            if not data:
                return None
            data.name = name
            data.updated_at = db.func.now()
         
            data.set_password(password)

            db.session.commit()

            return data
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def update_users_status(id, status):
        try:
            user = User.query.get(id)
            if not user:
                return None

            user.status = status
            user.updated_at = db.func.now()

            db.session.commit()

            return user
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def update_users_password(id, password):
        try:
            user = User.query.get(id)
            if not user:
                return None

            user.set_password(password)
            user.updated_at = db.func.now()

            db.session.commit()

            return user
        except Exception as e:
            db.session.rollback()
            return e

    @staticmethod
    def delete_users(id):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user