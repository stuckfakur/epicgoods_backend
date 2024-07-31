from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    
    def to_dict(self):
        return{
            'id' : self.id,
            'username' : self.username
        }
    
    
    
    def __repr__(self) -> str:
        return f"<User {self.name}>"