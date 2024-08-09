from . import db

class Seller(db.Model):
    __tablename__ = 'sellers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    location_id = db.Column(db.ForeignKey('locations.id'))
    store_name = db.Column(db.String(80))
    store_type = db.Column(db.String(2), default='0')
    store_info = db.Column(db.String(1000))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def to_dict(self):
        return{
            'id' : self.id,
            'user_id' : self.user_id,
            'location_id' : self.location_id,
            'store_name': self.store_name,
            'store_type' : self.store_type,
            'store_info' : self.store_info,
            'description' : self.description,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }
    
    def __repr__(self) -> str:
        return f"<Seller {self.store_name}>"