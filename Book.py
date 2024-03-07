"""Book Class
Create a Book class to represent each book with attributes like title, author, ISBN, quantity, etc.
Implement methods for adding, updating, and removing books.
Include a method to display book details."""
class Book:
    #initialize instance variables, default quantity is 1
    def __init__(self, title, author, isbn, quantity=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
    
    def update_quantity(self, amount):
        self.quantity = amount
    #update info about a book object, nothing happens if no params are passed
    def update(self, title = None, author = None, isbn = None):
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn
            
    #display details
    def display(self):
        print(f"{self.title},{self.author},{self.isbn},{self.quantity}")
        
    #remove object method
    def remove(self):
        del self