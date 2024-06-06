from flask import Blueprint, request, jsonify
from models import Book
from database import db

bp = Blueprint('library', __name__)

@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.__dict__ for book in books if '_sa_instance_state' in book.__dict__ and book.__dict__.pop('_sa_instance_state', None) is not None])

@bp.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if book:
        return jsonify(book.__dict__)
    return {'message': 'Book not found'}, 404

@bp.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], published_date=data.get('published_date'), isbn=data['isbn'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.__dict__), 201

@bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if book:
        data = request.json
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.published_date = data.get('published_date', book.published_date)
        book.isbn = data.get('isbn', book.isbn)
        db.session.commit()
        return jsonify(book.__dict__)
    return {'message': 'Book not found'}, 404

@bp.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return {'message': 'Book deleted'}
    return {'message': 'Book not found'}, 404
