class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library:

    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        if book not in self._books:
            book.is_checked_out = True
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.is_checked_out = False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.is_checked_out = True

    def list_available_books(self):
        for book in self._books:
            if book.is_checked_out == True:
                print(f"{book.title} by {book.author}")