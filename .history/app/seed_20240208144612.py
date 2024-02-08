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
    
    ]



    for quote_data in quotes_data:
        quote = Quote(**quote_data)
        db.session.add(quote)
    db.session.commit()


    authors = [
    {"name": "Unknown", "nationality": ""},
    {"name": "Abraham Lincoln", "nationality": "American"},
    {"name": "Nelson Mandela", "nationality": "South African"},
    {"name": "Winston Churchill", "nationality": "British"},
    {"name": "Steve Jobs", "nationality": "American"},
    {"name": "Albert Einstein", "nationality": "German-American"},
    {"name": "Franklin D. Roosevelt", "nationality": "American"},
    {"name": "Confucius", "nationality": "Chinese"},
    {"name": "Theodore Roosevelt", "nationality": "American"},
    {"name": "Vince Lombardi", "nationality": "American"},
    {"name": "Ralph Waldo Emerson", "nationality": "American"},
    {"name": "George Bernard Shaw", "nationality": "Irish"},
    {"name": "George Eliot", "nationality": "British"},
    {"name": "Wayne Gretzky", "nationality": "Canadian"},
   

    print("📚 Done seeding!")
