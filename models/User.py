from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    # seller_id = db.Column(db.Integer, ForeignKey("seller.id"))
    status = db.Column(db.String(2), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def to_dict(self):
        return{
            'id' : self.id,
            'username' : self.username,
            'email' : self.email,
            'password' : self.password,
            # 'seller_id' : self.seller_id,
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