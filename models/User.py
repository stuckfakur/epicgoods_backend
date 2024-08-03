from . import db
from flask_login import UserMixin
import bcrypt
from sqlalchemy import ForeignKey

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    consumer_data =db.Column(db.Text)
    isSeller = db.Column(db.String(2), default='0')
    seller_id = db.Column(db.Integer, ForeignKey("seller"))
    status = db.Column(db.String(2), default='1')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def to_dict(self):
        return{
            'id' : self.id,
            'name': self.name,
            'username' : self.username,
            'email' : self.email,
            'password' : self.password,
            'consumer_data' : self.consumer_data,
            'isSaller' : self.isSeller,
            'seller_id' : self.seller_id,
            'status' : self.status,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }
    
    

    def __repr__(self) -> str:
        return f"<User {self.name}>"

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))