from models.User import User, db

class UserRepository:
    
    @staticmethod
    def get_all_users():
        return User.query.all()