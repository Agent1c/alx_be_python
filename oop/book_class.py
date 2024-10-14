class Book:
    """Class Book/Constructor Declaration, with 3 parameter"""
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    """Destructor Declaration, deleting the title"""
    def __del__(self):
        print(f"Deleting {self.title}")
    
    """String Representation - Returns a string in the format"""
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    """Official Representation, recreate the Book instance"""
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"