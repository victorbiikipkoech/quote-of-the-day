from app import app, db
from models import Quote, Author,Category
from faker import Faker

def seed_database():
    fake = Faker()
    with app.app_context():
        # Delete existing quotes data
        Quote.query.delete()

        # New quotes data
        quotes = [
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

        # Collect author names and check existence in a single query
        author_names = {fake.name() for _ in range(len(quotes_data))}
        existing_authors = {author.name for author in Author.query.filter(Author.name.in_(author_names))}
        new_authors = [Author(name=name) for name in author_names if name not in existing_authors]

        # Add new authors to the session
        db.session.add_all(new_authors)
        db.session.flush()  # Generate primary key IDs for new authors

        # Add new quotes to the database
        for quote_info, author_name in zip(quotes_data, author_names):
            quote_text = quote_info['text']
            author = next(author for author in new_authors if author.name == author_name)
            quote = Quote(text=quote_text, author=author)
            db.session.add(quote)

        # Commit all changes to the database
        db.session.commit()

if __name__ == "__main__":
    seed_database()
