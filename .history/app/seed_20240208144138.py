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

    authors_data = [
        {"name": "Harper Lee", "nationality": "American"},
        {"name": "George Orwell", "nationality": "British"},
        {"name": "F. Scott Fitzgerald", "nationality": "American"},
        {"name": "Jane Austen", "nationality": "British"},
        {"name": "J.K. Rowling", "nationality": "British"},
    ]

    for author_data in authors_data:
        author = Author(**author_data)
        db.session.add(author)
    db.session.commit()

    quotes_data = [
        {"text": "A thought-provoking classic.", "author_id": 1},
        {"text": "A dystopian masterpiece.", "author_id": 2},
        {"text": "A captivating tale of love and tragedy.", "author_id": 3},
        {"text": "A delightful comedy of manners.", "author_id": 4},
        {"text": "A magical adventure for all ages.", "author_id": 5},
    ]

    for quote_data in quotes_data:
        quote = Quote(**quote_data)
        db.session.add(quote)
    db.session.commit()

    categories_data = [
        {"name": "To kill a Mockingbird", "description": "Timeless literary works", "author_id": 1},
        {"name": "1984", "description": "Dangers of totalitarianism", "author_id": 2},
        {"name": "The Great Gatsby", "description": "Books portraying a nightmare world", "author_id": 3},
        {"name": "Pride and Prejudice", "description": "Books focused on romantic relationships", "author_id": 4},
        {"name": "Harry Potter and the Sorcerer's Stone", "description": "Books with elements of magic and fantasy", "author_id": 5},
    ]
    for category_data in categories_data:
        category = Category(**category_data)
        db.session.add(category)
    db.session.commit()

    print("📚 Done seeding!")
