from repositories.UserRepository import UserRepository
from utils.exception import NotFoundError
from flask_jwt_extended import get_jwt_identity
from sqlalchemy.exc import DataError
from models.ProductCart import ProductCart
from repositories.ProductCartRepository import ProductCartRepository
import re

class Validator:
    @staticmethod
    def user_validator(name, email, password):
        if not name or not isinstance(name, str):
            raise ValueError("Name is required")
        if not email or not isinstance(email, str):
            raise ValueError("Email is required")
        if not password or not isinstance(password, str):
            raise ValueError("Password is required")



        regex_email = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        if not re.match(regex_email, email):
            raise ValueError('please input the valid email')

    @staticmethod
    def extra_validator(username, status, consumer_data):
        if not username or not isinstance(username, str):
            raise ValueError("Username is required")
        if not status or not isinstance(status, str):
            raise ValueError("Status is required")
        if not consumer_data or not isinstance(consumer_data, str):
            raise ValueError("Consumer data is required")

        regex_username = '^[a-zA-Z0-9]*$'
        if not re.match(regex_username, username):
            raise ValueError('only alpabeth and number is allowed in username')

    @staticmethod
    def user_existing_username(username):
        if UserRepository.user_existing_username(username):
            raise ValueError('username already exist')

    @staticmethod
    def user_existing_email(email):
        if UserRepository.user_existing_email(email):
            raise ValueError('email already exist')

class UserService:
    @staticmethod
    def create_users(
        name,
        email,
        password,
    ):
        Validator.user_validator(name, email, password)
        Validator.user_existing_email(email)
        return UserRepository.create_users(
            name,
            email,
            password,
        )

    @staticmethod
    def get_user_by_email(email):
        return UserRepository.user_existing_email(email)

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
    def get_mydata_user():
        id = get_jwt_identity()['id']
        find_data = UserRepository.get_users_by_id(id)
        if not find_data:
            raise NotFoundError('user not found')

        data = UserRepository.get_mydata_users(id)
        return data

    @staticmethod
    def update_users(userId, name, username, email, password, status, consumer_data):
        Validator.user_validator(name, email, password)
        Validator.extra_validator(username, status, consumer_data)
        user = UserService.get_users_by_id(userId)
        if not user:
            raise NotFoundError("User not found")
        try:
            user = UserRepository.update_users(
                userId,
                name,
                username,
                email,
                password,
                status,
                consumer_data
            )
            return user.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
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
    def update_users_is_seller(id, is_seller):
        data = UserService.get_users_by_id(id)
        if not data:
            raise NotFoundError('user not found')

        user = UserRepository.update_users_is_seller(id, is_seller)
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

    @staticmethod
    def get_user_cart():
        user_id = get_jwt_identity()['id']  # Mendapatkan ID pengguna dari token JWT
        
        # Mengambil data pengguna dan cart produk berdasarkan ID pengguna
        user = UserRepository.get_user_by_id(user_id)
        if user is None:
            raise NotFoundError('User not found')
        
        cart_items = ProductCartRepository.get_product_cart_by_user_id(user_id)
        
        # Mengembalikan data cart produk
        return [item.to_dict() for item in cart_items]  # Sesuaikan dengan metode model Anda
