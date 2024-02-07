#!/usr/bin/env python3

from app import app, db
from models import Quote, Author

with app.app_context():
    # Delete existing quotes and authors data
    Quote.query.delete()
    Author.query.delete()

    # New authors data
    authors_data = [
        {"name": "Steve Jobs"},
        {"name": "Abraham Lincoln"},
        {"name": "Nelson Mandela"},
        {"name": "Winston Churchill"},
        {"name": "Albert Einstein"},
        {"name": "Franklin D. Roosevelt"},
        {"name": "Confucius"},
        {"name": "Theodore Roosevelt"},
        {"name": "Vince Lombardi"},
        {"name": "Ralph Waldo Emerson"},
        {"name": "Booker T. Washington"},
        {"name": "George Eliot"},
        {"name": "Peter Drucker"},
        {"name": "Wayne Gretzky"},
        {"name": "Mark Twain"},
        {"name": "Carl Rogers"},
        {"name": "Eleanor Roosevelt"},
        {"name": "Sam Levenson"},
        {"name": "Mahatma Gandhi"},
        {"name": "Socrates"},
        {"name": "Oscar Wilde"},
        {"name": "Plato"},
        {"name": "Christopher Columbus"},
        {"name": "Lao Tzu"},
        {"name": "George Bernard Shaw"},
        {"name": "Babe Ruth"}
    ]

    # Add new authors to the database
    for author_info in authors_data:
        author = Author(**author_info)
        db.session.add(author)

    db.session.commit()

    # New quotes data
    quotes_data = [
        {"text": "The only way to do great work is to love what you do.", "author_id": 1},
        {"text": "In the end, it's not the years in your life that count. It's the life in your years.", "author_id": 2},
        {"text": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author_id": 3},
        {"text": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author_id": 4},
        {"text": "Your time is limited, so don't waste it living someone else's life.", "author_id": 1},
        {"text": "Life is like riding a bicycle. To keep your balance, you must keep moving.", "author_id": 5},
        {"text": "The only limit to our realization of tomorrow will be our doubts of today.", "author_id": 6},
        {"text": "It does not matter how slowly you go as long as you do not stop.", "author_id": 7},
        {"text": "Believe you can and you're halfway there.", "author_id": 8},
        {"text": "It's not whether you get knocked down, it's whether you get up.", "author_id": 9},
        {"text": "Strive not to be a success, but rather to be of value.", "author_id": 5},
        {"text": "The only person you are destined to become is the person you decide to be.", "author_id": 10},
        {"text": "If you want to lift yourself up, lift up someone else.", "author_id": 11},
        {"text": "It is never too late to be what you might have been.", "author_id": 12},
        {"text": "Do not go where the path may lead, go instead where there is no path and leave a trail.", "author_id": 10},
        {"text": "The best way to predict the future is to create it.", "author_id": 13},
        {"text": "You miss 100% of the shots you don’t take.", "author_id": 14},
        {"text": "Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do.", "author_id": 15},
        {"text": "The only person who is educated is the one who has learned how to learn …and change.", "author_id": 16},
        {"text": "There is no passion to be found playing small – in settling for a life that is less than the one you are capable of living.", "author_id": 3},
        {"text": "The future belongs to those who believe in the beauty of their dreams.", "author_id": 17},
        {"text": "Don’t watch the clock; do what it does. Keep going.", "author_id": 18},
        {"text": "You must be the change you wish to see in the world.", "author_id": 19},
        {"text": "The only true wisdom is in knowing you know nothing.", "author_id": 20},
        {"text": "Be yourself; everyone else is already taken.", "author_id": 21},
        {"text": "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light.", "author_id": 22},
        {"text": "You can never cross the ocean until you have the courage to lose sight of the shore.", "author_id": 23},
        {"text": "A journey of a thousand miles begins with a single step.", "author_id": 24},
        {"text": "Life isn’t about finding yourself. Life is about creating yourself.", "author_id": 25},
        {"text": "Every strike brings me closer to the next home run.", "author_id": 26}
    ]

    # Add new quotes to the database
    for quote_info in quotes_data:
        quote = Quote(**quote_info)
        db.session.add(quote)

    db.session.commit()
