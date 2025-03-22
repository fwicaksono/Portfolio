# library.py

# 1. Definisikan class Book
class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"{self.title} telah dipinjam"
        return f"maaf, {self.title} sedang dipinjam"
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"Terimakasih, {self.title} telah dikembalikan"
        return f"{self.title} sudah didikembalikan"


# 2. Definisikan class Library
class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)
        
    def list_books(self):
        available_books = []
        for book in self.book_list:  # Looping semua buku dalam perpustakaan
            if not book.is_borrowed:  # Cek apakah buku belum dipinjam
                available_books.append(book.title)  # Tambahkan judul buku ke daftar
                 
        if available_books:
            for book in available_books:
                print(f"- {book}")
        else:
            print("Tidak ada buku yang tersedia.")
            
    def borrow_book(self, title):
        for book in self.book_list:
            if book.title == title:
                print(book.borrow())
                return
        print(f"Buku '{title}' tidak ditemukan di perpustakaan.")

    def return_book(self, title):
        for book in self.book_list:
            if book.title == title:
                print(book.return_book())
                return
        print(f"Buku '{title}' tidak ditemukan di perpustakaan.")

# 3. Fungsi utama untuk mengetes kode
if __name__ == "__main__":
    library = Library()

    # Tambahkan beberapa buku ke perpustakaan
    book1 = Book("Python Dasar")
    book2 = Book("Machine Learning")
    book3 = Book("Data Engineering")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # List semua buku yang tersedia
    library.list_books()

    # Coba pinjam buku
    library.borrow_book("Python Dasar")
    library.borrow_book("Machine Learning")

    # List ulang setelah peminjaman
    library.list_books()

    # Coba kembalikan buku
    library.return_book("Python Dasar")

    # List ulang setelah pengembalian
    library.list_books()
