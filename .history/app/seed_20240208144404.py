from models import db, Quote, Author, Category
from app import app

with app.app_context():
    print("🗑️ Removing existing seed data...")

    # Delete existing records in the quotes table
    db.session.query(Quote).delete()

    # Delete existing records in the authors table
    db.session.query(Author).delete()

    # Delete existing records in the category table
    db.session.query(Category).delete()

    db.session.commit()
    print("🗑️ Existing seed data removed.")

    print("📚 Seeding quotes with reviews...")

    quotes_data = [
        {"text": "The only way to do great work is to love what you do."},
        {"text": "In the end, it's not the years in your life that count. It's the life in your years."},
        {"text": "The greatest glory in living lies not in never falling, but in rising every time we fall."},
        {"text": "Success is not final, failure is not fatal: It is the courage to continue that counts."},
        {"text": "Your time is limited, so don't waste it living someone else's life."},
        {"text": "Life is like riding a bicycle. To keep your balance, you must keep moving."},
        {"text": "The only limit to our realization of tomorrow will be our doubts of today."},
        {"text": "It does not matter how slowly you go as long as you do not stop."},
        {"text": "Believe you can and you're halfway there."},
        {"text": "It's not whether you get knocked down, it's whether you get up."},
        {"text": "Strive not to be a success, but rather to be of value."},
        {"text": "The only person you are destined to become is the person you decide to be."},
        {"text": "If you want to lift yourself up, lift up someone else."},
        {"text": "It is never too late to be what you might have been."},
        {"text": "Do not go where the path may lead, go instead where there is no path and leave a trail."},
        {"text": "The best way to predict the future is to create it."},
        {"text": "You miss 100% of the shots you don’t take."},
        {"text": "Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do."},
        {"text": "The only person who is educated is the one who has learned how to learn …and change."},
        {"text": "There is no passion to be found playing small – in settling for a life that is less than the one you are capable of living."},
        {"text": "The future belongs to those who believe in the beauty of their dreams."},
        {"text": "Don’t watch the clock; do what it does. Keep going."},
        {"text": "You must be the change you wish to see in the world."},
        {"text": "The only true wisdom is in knowing you know nothing."},
        {"text": "Be yourself; everyone else is already taken."},
        {"text": "We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light."},
        {"text": "You can never cross the ocean until you have the courage to lose sight of the shore."},
        {"text": "A journey of a thousand miles begins with a single step."},
        {"text": "Life isn’t about finding yourself. Life is about creating yourself."},
        {"text": "Every strike brings me closer to the next home run."}
    ]

    for quote_data in quotes_data:
        quote = Quote(**quote_data)
        db.session.add(quote)
    db.session.commit()

    print("📚 Done seeding!")
