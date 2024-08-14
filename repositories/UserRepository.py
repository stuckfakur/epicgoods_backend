from models.User import User, db
import random


class UserRepository:

    @staticmethod
    def create_users(
            name,
            email,
            password,
    ):
        random_number = random.randint(1000, 9999)
        username = f"{name.replace(' ', '_')}_{random_number}"
        while User.query.filter_by(username=username).first():
            random_number = random.randint(1000, 9999)
            username = f"{name.replace(' ', '_')}_{random_number}"

        new_user = User(
            name=name,
            username=username,
            email=email,
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
    def user_existing_email(email, user_id=None):
        existing = User.query.filter_by(email=email)
        if user_id:
            existing = existing.filter(User.id != user_id)

        existing = existing.first()
        return True if existing else False

    @staticmethod
    def user_existing_username(username, user_id=None):
        existing = User.query.filter_by(username=username)
        if user_id:
            existing = existing.filter(User.id != user_id)

        existing = existing.first()
        return True if existing else False

    @staticmethod
    def update_users(id, name, username, email,password, consumer_data, status, is_seller):
        try:
            user = User.query.get(id)
            if not user:
                return None
            
            user.name = name
            user.username = username
            user.consumer_data = consumer_data
            user.status = status
            user.is_seller = is_seller
            user.updated_at = db.func.now()

            if email and email != user.email:
                if UserRepository.check_email_exist(email, id):
                    raise ValueError('email already exist')
            if email:
                user.email = email

            db.session.commit()

            return user
        except Exception as e:
            db.session.rollback()
            return e

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
    def update_users_is_seller(id, is_seller):
        try:
            user = User.query.get(id)
            if not user:
                return None

            user.is_seller = is_seller
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
