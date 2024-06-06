from database import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    published_date = db.Column(db.String(20))
    isbn = db.Column(db.String(13), unique=True, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'
