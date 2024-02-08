from models import db, Quote, Author, Category
from app import app

with app.app_context():



    quotes_data = [
      
        {"text": "In the end, it's not the years in your life that count. It's the life in your years.","author_id":1},
        {"text": "The greatest glory in living lies not in never falling, but in rising every time we fall.","author_id":2},
        {"text": "Success is not final, failure is not fatal: It is the courage to continue that counts.","author_id":3},
        {"text": "Your time is limited, so don't waste it living someone else's life.","author_id":4},
        {"text": "Life is like riding a bicycle. To keep your balance, you must keep moving.","author_id":5},
        {"text": "The only limit to our realization of tomorrow will be our doubts of today.","author_id":6},

    
    ]



    for quote_data in quotes_data:
        quote = Quote(**quote_data)
        db.session.add(quote)
    db.session.commit()


    authors_data = [
    
    {"name": "Abraham Lincoln", "nationality": "American"},
    {"name": "Nelson Mandela", "nationality": "South African"},
    {"name": "Winston Churchill", "nationality": "British"},
    {"name": "Steve Jobs", "nationality": "American"},
    {"name": "Albert Einstein", "nationality": "German-American"},
    {"name": "Franklin D. Roosevelt", "nationality": "American"},
 
    ]
    for author_data in authors_data:
        author=Author(**author_data)
        db.session.add(author)
    db.session.commit()

  category_data = [
    {"name": "Motivational Quotes", "description": "Inspirational quotes to uplift spirits", "author_id": 1},
    {"name": "Philosophical Quotes", "description": "Quotes that delve into deep thoughts", "author_id": 2},
    {"name": "Life Quotes", "description": "Quotes about the journey of life", "author_id": 3},
    {"name": "Success Quotes", "description": "Quotes about achieving goals and success", "author_id": 4},
    {"name": "Courage Quotes", "description": "Quotes about bravery and overcoming fear", "author_id": 5},
]

for category_data in categories_data:
    category = Category(**category_data)
    db.session.add(category)

db.session.commit()

    print("📚 Done seeding!")
