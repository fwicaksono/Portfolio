import logging

# Konfigurasi logging
logging.basicConfig(
    filename="transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            log_message = f"{self.name} borrowed {book.title}"
            logging.info(log_message)  # Mencatat transaksi ke log
            return log_message
        return f"{book.title} is not available"

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            log_message = f"{self.name} returned {book.title}"
            logging.info(log_message)  # Mencatat transaksi ke log
            return log_message
        return f"{self.name} did not borrow {book.title}"