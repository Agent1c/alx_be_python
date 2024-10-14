class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author , file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = [] # Initialize the books list

    def add_book(self, book):
        self.books.append(book) # Append the book to the instance's book list

    def list_books(self):
        for book in self.books:
            # Check if it's an instance of PrintBook to access page_count
            if isinstance(book, PrintBook):
                print(f"Title: {book.title}, Author: {book.author}, Pages: {book.page_count}")
            else:
                print(f"Title: {book.title}, Author: {book.author}, File Size: {book.file_size}")
        
