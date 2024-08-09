from models.User import User, db

class UserRepository:

    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def get_users_by_id(id):
        return User.query.get(id)

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
    def update_users(id, data):
        user = User.query.get(id)
        if user:
            for key, value in data.items():
                setattr(user, key, value)
            db.session.commit()
        return user

    @staticmethod
    def delete_users(id):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user