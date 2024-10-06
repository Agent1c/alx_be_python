class Book:

    """Book Initializing Class"""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    """Check Out method"""
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    """Returning Availability Books """
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    """Shows what books in the Library"""
    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self, _books):
        self._books = []
    """Library Init"""
    def add_book(self, books):
        self._books.append(books)

    """Checking out books out of Library"""
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return book.author
                else:
                    return title
                
        return 

    """Returning/restoring a book into library"""
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return title
                else:
                    return title
        return title

    """Listing available/left books in library"""
    def list_available_books(self, title):
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            return "Available books: " + ", ".join(available_books)
        else:
            return "No books are currently available."

