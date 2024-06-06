import unittest
from app import create_app
from database import db
from models import Book

class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_add_book(self):
        response = self.client.post('/books', json={
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2024',
            'isbn': '1234567890123'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['title'], 'Test Book')

    def test_get_books(self):
        response = self.client.post('/books', json={
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2024',
            'isbn': '1234567890123'
        })
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test Book')

    def test_get_book(self):
        response = self.client.post('/books', json={
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2024',
            'isbn': '1234567890123'
        })
        self.assertEqual(response.status_code, 201)
        book_id = response.get_json()['id']
        response = self.client.get(f'/books/{book_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['title'], 'Test Book')

    def test_update_book(self):
        response = self.client.post('/books', json={
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2024',
            'isbn': '1234567890123'
        })
        self.assertEqual(response.status_code, 201)
        book_id = response.get_json()['id']
        response = self.client.put(f'/books/{book_id}', json={
            'title': 'Updated Book'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['title'], 'Updated Book')

    def test_delete_book(self):
        response = self.client.post('/books', json={
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2024',
            'isbn': '1234567890123'
        })
        self.assertEqual(response.status_code, 201)
        book_id = response.get_json()['id']
        response = self.client.delete(f'/books/{book_id}')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(f'/books/{book_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
