# main.py
from library import Library
from book import Book
from member import Member

library = Library()
library.add_book(Book("Python 101", "John Doe", "123456789"))
library.add_book(Book("Data Science Basics", "Jane Smith", "987654321"))

member1 = Member("Alice", 1)
library.add_member(member1)

print(library.list_books())
print(member1.borrow_book(library.books[0]))
print(library.list_books())
print(member1.return_book(library.books[0]))
print(library.list_books())
