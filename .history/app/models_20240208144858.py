from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Quote(db.Model, SerializerMixin):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
  
   
    author = db.relationship('Author', backref='quotes')
 

    def serialize(self):
        return {'id': self.id, 'text': self.text, 'author_id': self.author_id, 'category_id': self.category_id}

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)

    author = db.relationship('Author', backref='categories')

    def serialize(self):
        return {'id': self.id, 'name': self.name, 'description': self.description}

class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    nationality = db.Column(db.String(150), nullable=False)

    def serialize(self):
        return {'id': self.id, 'name': self.name, 'nationality': self.nationality}
