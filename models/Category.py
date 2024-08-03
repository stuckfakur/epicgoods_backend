from . import db
from flask_login import UserMixin

class Category(UserMixin, db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_slug = db.Column(db.String(80), unique=True)
    category_name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def to_dict(self):
        return{
            'id' : self.id,
            'category_slug': self.category_slug,
            'category_name': self.category_name,
            'description' : self.description,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }
    
    def __repr__(self) -> str:
        return f"<Category {self.category_name}>"