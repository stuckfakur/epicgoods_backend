from repositories.UserRepository import UserRepository

class UserService:
    @staticmethod
    def get_all_users():
        users = UserRepository.get_all_users()
        return [user.to_dict() for user in users]