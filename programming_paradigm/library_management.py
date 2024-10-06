class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
    
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} by {self.author} is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} by {self.author} has been returned.")
        else:
            print(f"{self.title} by {self.author} was not checked out.")

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