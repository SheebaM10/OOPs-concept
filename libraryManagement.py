# Library Management System Class: Book (title, author, available) Class: Library (a list of books). Methods: add_book(),
# borrow_book(title),return_book(title),show_available_books()

class Book:
    def __init__(self,title, author):
        self.title= title
        self.author=author
        self.available= True    
        
class Library:
    def __init__(self):
        self.books=[]
        
        
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added: {title} by {author}")
        
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f"  You borrowed: {title}")
                return
        print("Book not available")
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f"  You returned: {title}")
                return
        print("Invalid return")
        
    def show_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(f"  {book.title} by {book.author}")
                
library = Library()
library.add_book("Python Basics", "Ram")
library.add_book("Data Science", "John")
library.show_available_books()
library.borrow_book("Python Basics")
library.show_available_books()
library.return_book("Python Basics")
library.show_available_books()