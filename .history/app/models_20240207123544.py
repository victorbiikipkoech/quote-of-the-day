from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
         return f"Author: {self.name}"

class Quote(db.Model, SerializerMixin):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    author = db.relationship('Author', backref='quotes')

    def __repr__(self):
         return f"Text: {self.text}, Author: {self.author.name}"
