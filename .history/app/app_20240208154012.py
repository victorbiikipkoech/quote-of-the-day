from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import Quote, Category, Author, db
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quote_of_the_day.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

migrate = Migrate(app, db)
api = Api(app)
db.init_app(app)

@app.route('/')
def home():
    return 'QUOTE_OF THE DAY'

class Quotes(Resource):
    def get(self):
        quotes = Quote.query.all()
        quote_dict = [quote.serialize() for quote in quotes]
        return jsonify(quote_dict)

api.add_resource(Quotes, '/quotes')

class QuotesById(Resource):
    def get(self, id):
        quote = Quote.query.get(id)
        if not quote:
            return {'error': 'Quote not found'}, 404
        return jsonify(quote.serialize())

    def delete(self, id):
        quote = Quote.query.get(id)
        if not quote:
            return{'error':'Quote id cannot be found'}, 404
        else:
            db.session.delete(quote)
            db.session.commit()
            response=make_response(jsonify({"message":"Record deleted successfully"}), 200)
            return response

api.add_resource(QuotesById, '/quotes/<int:id>')


class Categories(Resource):
    def get(self):
        categories = Category.query.all()
        category_dict = [category.serialize() for category in categories]
        return jsonify(category_dict)

api.add_resource(Categories, '/categories')

class CategoriesById(Resource):
    def get(self, id):
        category = Category.query.get(id)
        if not category:
            return {'error': 'Category not found'}, 404
        return jsonify(category.serialize())

    def patch(self, id):
        data = request.get_json()
        name = data['name']
        description = data['description']
        genre = data['genre']
        category = Category.query.get(id)
        if not category:
            return {'error': 'Category not found'}, 404
        else:
            category.name = name
            category.description = description
            category.genre = genre
            db.session.commit()

            response = make_response(jsonify(category.serialize()),200)
            return response

            # response=make_response(jsonify(category.serialize()),200)
            # return response

api.add_resource(CategoriesById, '/categories/<int:id>')

class Authors(Resource):
    def post(self):
        data = request.get_json()
        name = data["name"]
        nationality = data["nationality"]

        if not Author:
            return {"error":"Author cannot be found"},400
        
        new_data = Author(name=name, nationality=nationality)
        db.session.add(new_data)
        db.session.commit()
        response=make_response (jsonify(new_data.serialize()), 201)
        return response

api.add_resource(Authors, '/authors')

if __name__== '_main_':
    app.run(port=5555