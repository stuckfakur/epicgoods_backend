from repositories.UserRepository import UserRepository
from utils.exception import NotFoundError
from flask_jwt_extended import get_jwt_identity

class Validator:
    @staticmethod
    def user_validator(name, username, email, password, consumer_data):
        if not name or not isinstance(name, str):
            raise ValueError("Name is required")
        if not username or not isinstance(username, str):
            raise ValueError("Username is required")
        if not email or not isinstance(email, str):
            raise ValueError("Email is required")
        if not password or not isinstance(password, str):
            raise ValueError("Password is required")
        if not consumer_data or not isinstance(consumer_data, str):
            raise ValueError("Consumer data is required")

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
    def get_mydata_user():
        id = get_jwt_identity()['id']
        find_data = UserRepository.get_users_by_id(id)
        if not find_data:
            raise NotFoundError('user not found')

        data = UserRepository.get_mydata_users(id)
        return data

    @staticmethod
    def update_users(id, name, password):
        Validator.user_validator(name, password)
        user = UserRepository.get_users_by_id(id)
        if user:
            return NotFoundError("User not found")
        try:
            user = UserRepository.update_users(
                id,
                name,
            )
            return user
        except Exception as e:
            raise e
        
    @staticmethod
    def update_users_status(id, status):
        data = UserService.get_users_by_id(id)
        if not data:
            raise NotFoundError('user not found')

        user = UserRepository.update_users_status(id, status)
        return user

    @staticmethod
    def update_users_password(id, password):
        data = UserService.get_users_by_id(id)
        if not data:
            raise NotFoundError('user not found')

        user = UserRepository.update_users_password(id, password)
        return user    

    @staticmethod
    def delete_users(id):
        user = UserRepository.get_users_by_id(id)
        if not user:
            raise NotFoundError("User not found")
        user = UserRepository.delete_users(id)
        return user