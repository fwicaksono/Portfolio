# library_management/book.py
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
