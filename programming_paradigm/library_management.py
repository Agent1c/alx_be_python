class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library(Book):
    def __init__(self, _books):
        self._books = []

    def add_book(self,_books):
        self._books.append(_books)

    # def remove_book(title):
    #     pass

    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out is True:
                    book._is_checked_out = False
                    return f"You've checked out {title} by {book.author}"
                else:
                    return "That book is currently checked out."
        return "We don't have that book in our library."

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out is False:
                    book._is_checked_out is True
                    return "That book is currently checked out."
                else:
                    return "That book is not currently checked out."
        return "We don't have that book in our library."

    def list_available_books(self, title):
        available_books = [self._books.title for book in self._books if book._is_checked_out is False]
        return ", ".join(available_books)

