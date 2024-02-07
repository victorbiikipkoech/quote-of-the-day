from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

db = SQLAlchemy(app)


class Quote(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    author = db.Column(db.String(100))

    def __repr__(self):
        return f"Quote(text='{self.text}', author='{self.author}')"


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the quote generator API"})


@app.route('/quotes', methods=['GET'])
def get_quotes():
    quotes = Quote.query.all()
    quotes_data = [{'id': quote.id, 'text': quote.text, 'author': quote.author} for quote in quotes]
    return make_response(jsonify(quotes_data), 200)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
