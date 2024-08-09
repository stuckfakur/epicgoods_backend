from repositories.UserRepository import UserRepository

class UserService:

    @staticmethod
    def get_all_users():
        users = UserRepository.get_all_users()
        return [user.to_dict() for user in users]
    
    @staticmethod
    def get_users_by_id(id):
        user = UserRepository.get_users_by_id(id)
        if user:
            return user.to_dict()
        else:
            return "User not found"
        
    @staticmethod
    def create_users(
        name,
        username,
        email,
        password,
        consumer_data
    ):
        return UserRepository.create_users(
            name,
            username,
            email,
            password,
            consumer_data
        )

    @staticmethod
    def update_users(id, data):
        user = UserRepository.get_users_by_id(id, data)
        if user:
            return user.to_dict()
        else:
            return None
        

    @staticmethod
    def delete_users(id):
        return UserRepository.delete_users(id)