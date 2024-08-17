from . import db
from flask_login import UserMixin

class Voucher(UserMixin, db.Model):
    __tablename__ = 'vouchers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    code = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(80), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    quota = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def to_dict(self):
        return{
            'id' : self.id,
            'name': self.name,
            'code': self.code,
            'type' : self.type,
            'value' : self.value,
            'quota' : self.quota,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }
    
    def __repr__(self) -> str:
        return f"<Voucher {self.name}>"