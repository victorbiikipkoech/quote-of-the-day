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
        {"text": "It's not whether you get knocked down, it's whether you get up.", "author": "Vince Lombardi"}
    ]

    # Add new quotes to the database
    for quote_info in quotes_data:
        quote = Quote(**quote_info)
        db.session.add(quote)

    db.session.commit()
