from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from models import Quote, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

db = SQLAlchemy(app)


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the quote generator API"})


@app.route('/quotes', methods=['GET'])
def get_quotes():
    quotes = Quote.query.all()
    quotes_data = [{'id': quote.id, 'text': quote.text, 'author': quote.author.name} for quote in quotes]
    return make_response(jsonify(quotes_data), 200)


if __name__ == '__main__':
    db.create_all()
    # Seed the database with quotes and authors
    from seed import seed_database
    seed_database()
    app.run(debug=True)
