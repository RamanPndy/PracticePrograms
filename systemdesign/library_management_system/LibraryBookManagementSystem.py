import unittest

class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = {}

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_available_books(self):
        print("Available Books:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Quantity: {book.quantity}")

    def borrow_book(self, user, title, quantity):
        for book in self.books:
            if book.title == title and book.quantity >= quantity:
                book.quantity -= quantity
                if title in user.borrowed_books:
                    user.borrowed_books[title] += quantity
                else:
                    user.borrowed_books[title] = quantity
                print(f"{user.name} borrowed {quantity} copies of {title}")
                return
        print(f"Sorry, {title} copies are not available")

    def return_book(self, user, title, quantity):
        if title in user.borrowed_books and user.borrowed_books[title] >= quantity:
            for book in self.books:
                if book.title == title:
                    book.quantity += quantity
                    user.borrowed_books[title] -= quantity
                    print(f"{user.name} returned {quantity} copies of {title}")
                    return
        print(f"You have not borrowed {quantity} copies of {title}")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Book {title} is available")
                return
        print(f"Book {title} is not available")

    def display_borrowed_books(self, user):
        print(f"{user.name}'s Borrowed Books:")
        for title, quantity in user.borrowed_books.items():
            print(f"Title: {title}, Quantity: {quantity}")

class TestLibraryBookManagement(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Book1", "Author1", 5)
        self.book2 = Book("Book2", "Author2", 3)
        self.user = User("User1")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_view_available_books(self):
        self.library.view_available_books()

    def test_borrow_book(self):
        self.library.borrow_book(self.user, "Book1", 2)
        self.assertEqual(self.book1.quantity, 3)

    def test_return_book(self):
        self.user.borrowed_books["Book1"] = 2
        self.library.return_book(self.user, "Book1", 1)
        self.assertEqual(self.book1.quantity, 4)

    def test_search_book(self):
        self.library.search_book("Book2")
        self.library.search_book("Book3")

    def test_display_borrowed_books(self):
        self.user.borrowed_books["Book1"] = 2
        self.user.borrowed_books["Book2"] = 1
        self.library.display_borrowed_books(self.user)

if __name__ == '__main__':
    unittest.main()
