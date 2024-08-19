from . import db

class Voucher(db.Model):
    __tablename__ = 'vouchers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voucher_name = db.Column(db.String(80), nullable=False)
    voucher_code = db.Column(db.String(80), unique=True, nullable=False)
    voucher_type = db.Column(db.String(80), nullable=False)
    voucher_value = db.Column(db.Integer, nullable=False)
    voucher_quota = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def to_dict(self):
        return{
            'id' : self.id,
            'voucher_name': self.voucher_name,
            'voucher_code': self.voucher_code,
            'voucher_type' : self.voucher_type,
            'voucher_value' : self.voucher_value,
            'voucher_quota' : self.voucher_quota,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }
    
    def __repr__(self) -> str:
        return f"<Voucher {self.id}>"