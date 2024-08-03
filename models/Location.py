from . import db
from flask_login import UserMixin

class Location(UserMixin, db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def to_dict(self):
        return{
            'id' : self.id,
            'location_name': self.location_name,
            'description' : self.description,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }
    
    def __repr__(self) -> str:
        return f"<Location {self.location_name}>"