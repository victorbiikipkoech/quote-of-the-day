from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from models import db, Quote  # Import db and Quote from your models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

db.init_app(app)  # Initialize the db instance with the app

# Define your routes here

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the quote generator API"})


@app.route('/quotes', methods=['GET'])
def get_quotes():
    quotes = Quote.query.all()
    quotes_data = [{'id': quote.id, 'text': quote.text, 'author': quote.author} for quote in quotes]
    return make_response(jsonify(quotes_data), 200)


if __name__ == '__main__':
    app.run(debug=True)
