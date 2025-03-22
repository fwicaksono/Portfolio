# library.py

# 1. Definisikan class Book
class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False
        
    def borrow(self):
        if not self.is_borrowed :
            self.is_borrowed = True
            return f"{self.title} telah dipinjam"
        return f"{self.title} sudah dipinjam"
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"{self.title} telah dikembalikan"
        return f"{self.title} sudah dikembalikan"


# 2. Fungsi utama untuk mengetes kode
if __name__ == "__main__":

    book1 = Book("Algoritma Pemrograman")
    print(book1.borrow())
    print(book1.borrow()) #harusnya muncul tidak bisa
    print(book1.return_book())
    print(book1.return_book()) #harusnya muncul sudah dikembalikan