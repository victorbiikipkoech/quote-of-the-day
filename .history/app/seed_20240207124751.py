#!/usr/bin/env python3

from app import app, db
from models import Quote  # Assuming you have a Quote model defined

with app.app_context():
    # Delete existing quotes data
    Quote.query.delete()

    # New quotes data
    quotes_data = [
        {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
        {"text": "In the end, it's not the years in your life that count. It's the life in your years.", "author": "Abraham Lincoln"},
        {"text": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": "Nelson Mandela"},
        {"text": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
        {"text": "Your time is limited, so don't waste it living someone else's life.", "author": "Steve Jobs"},
        {"text": "Life is like riding a bicycle. To keep your balance, you must keep moving.", "author": "Albert Einstein"},
        {"text": "The only limit to our realization of tomorrow will be our doubts of today.", "author": "Franklin D. Roosevelt"},
        {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
        {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
        {"text": "It's not whether you get knocked down, it's whether you get up.", "author": "Vince Lombardi"},
        {"text": "Strive not to be a success, but rather to be of value.", "author": "Albert Einstein"},
        {"text": "The only person you are destined to become is the person you decide to be.", "author": "Ralph Waldo Emerson"},
        {"text": "If you want to lift yourself up, lift up someone else.", "author": "Booker T. Washington"},
        {"text": "It is never too late to be what you might have been.", "author": "George Eliot"},
        {"text": "Do not go where the path may lead, go instead where there is no path and leave a trail.", "author": "Ralph Waldo Emerson"},
        {"text": "The best way to predict the future is to create it.", "author": "Peter Drucker"},
        {"text": "You miss 100% of the shots you don’t take.", "author": "Wayne Gretzky"},
        {"text": "Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do.", "author": "Mark Twain"},
        {"text": "The only person who is educated is the one who has learned how to learn …and change.", "author": "Carl Rogers"},
        {"text": "There is no passion to be found playing small – in settling for a life that is less than the one you are capable of living.", "author": "Nelson Mandela"},
        {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
        {"text": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
        {"text": "You must be the change you wish to see in the world.", "author": "Mahatma Gandhi"},
        {"text": "The only true wisdom is in knowing you know nothing.", "author": "Socrates"},
        {"text": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
        {"text": "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light.", "author": "Plato"},
        {"text": "You can never cross the ocean until you have the courage to lose sight of the shore.", "author": "Christopher Columbus"},
        {"text": "A journey of a thousand miles begins with a single step.", "author": "Lao Tzu"},
        {"text": "Life isn’t about finding yourself. Life is about creating yourself.", "author": "George Bernard Shaw"},
        {"text": "Every strike brings me closer to the next home run.", "author": "Babe Ruth"}
    ]

    # Add new quotes to the database
    for quote_info in quotes_data:
        quote = Quote(**quote_info)
        db.session.add(quote)

    db.session.commit()
