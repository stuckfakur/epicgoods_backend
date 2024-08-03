from repositories.UserRepository import UserRepository

class UserService:
    @staticmethod
    def get_all_users():
        users = UserRepository.get_all_users()
        return [user.to_dict() for user in users]
    
    @staticmethod
    def get_user_by_id(id):
        return UserRepository.get_user_by_id(id)

    @staticmethod
    def create_users(
        name,
        username,
        email,
        password,
        consumer_data
    ):
        return UserRepository.create_user(
            name,
            username,
            email,
            password,
            consumer_data
        )

    @staticmethod
    def update_user(user_id, data):
        return UserRepository.update_user(user_id, data)

    @staticmethod
    def delete_user(user_id):
        return UserRepository.delete_user(user_id)