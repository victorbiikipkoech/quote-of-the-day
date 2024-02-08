from models import db, Book, Author,Category
from app import app

with app.app_context():
    print("🗑️ Removing existing seed data...")

    # Delete existing records in the books table
    db.session.query(Book).delete()

    # Delete existing records in the authors table
    db.session.query(Author).delete()
    # Delete existing records in the category table
    db.session.query(Category).delete()

    db.session.commit()
    print("🗑️ Existing seed data removed.")

    print("📚 Seeding books with reviews...")

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

    books_data = [
        {"title": "To Kill a Mockingbird", "review": "A thought-provoking classic.", "author_id": 1, "image_url": "https://books.google.co.ke/books/publisher/content?id=_LyTCgAAQBAJ&pg=PP1&img=1&zoom=3&hl=en&bul=1&sig=ACfU3U2PDUkjLubxyTF74uFMhClFwC_0nQ&w=1280"},
        {"title": "1984", "review": "A dystopian masterpiece.", "author_id": 2, "image_url": "https://mir-s3-cdn-cf.behance.net/project_modules/hd/c9448933546269.57a20fb97b03d.jpg"},
        {"title": "The Great Gatsby", "review": "A captivating tale of love and tragedy.", "author_id": 3, "image_url": "https://www.thecommononline.org/wp-content/uploads/2013/06/Screen-Shot-2017-05-31-at-2.19.46-PM.png"},
        {"title": "Pride and Prejudice", "review": "A delightful comedy of manners.", "author_id": 4, "image_url": "https://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg"},
        {"title": "Harry Potter and the Sorcerer's Stone", "review": "A magical adventure for all ages.", "author_id": 5, "image_url": "https://upload.wikimedia.org/wikipedia/en/7/7a/Harry_Potter_and_the_Philosopher%27s_Stone_banner.jpg"},
    ]

    for book_data in books_data:
        book = Book(**book_data)
        db.session.add(book)
    db.session.commit()


    categories_data = [
        {"name": "To kill a Mockingbird", "description": "Timeless literary works", "genre": "Thriller","author_id":1},
        {"name": "1984" , "description": "Dangers of totalitaranism", "genre": "Dystopian","author_id":2},
        {"name": "The Great Gatsby", "description": "Books portraying a nightmare world", "genre": "Dystopian","author_id":3},
        {"name": "Pride and Prejudice", "description": "Books focused on romantic relationships", "genre": "Romance","author_id":4},
        {"name": "Harry Potter and the Sorcerer's Stone", "description": "Books with elements of magic and fantasy", "genre": "Fantasy","author_id":5},
    ]
    for category_data in categories_data:
        category=Category(**category_data)
        db.session.add(category)
    db.session.commit()

    print("📚 Done seeding!")