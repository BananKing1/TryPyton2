"""
Studera följande kod. Ändra gärna och experimentera och se vad som händer. 
"""

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
 
    def add_book(self, book):
        self.books.append(book)
 
    def get_books(self):
        return self.books
 
    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
 
    def remove_book(self, title):
        book = self.get_book(title)
        if book:
            self.books.remove(book)
 
    def __str__(self):
        return f"Library {self.name} with {len(self.books)} books"
 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
 
    def __str__(self):
        return f"Book {self.title} by {self.author}"
 
if __name__ == "__main__":
 
    library = Library("My library")
 
    book1 = Book("The Hobbit", "J.R.R. Tolkien")
    book2 = Book("The Lord of the Rings", "J.R.R. Tolkien")
    book3 = Book("The Silmarillion", "J.R.R. Tolkien")
 
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
 
    print(library)
 
    library.remove_book("The Hobbit")
 
    print(library)
 
    print(library.get_book("The Lord of the Rings"))
 
    print(library.get_book("The Hobbit"))
 
    #print books the readable way
    for book in library.get_books():
        print(book)
 
    print(library.get_books()[0])