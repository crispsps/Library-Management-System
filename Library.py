"""Library Class
Design a Library class to manage the overall library system.
Include methods for searching books, managing patrons, handling transactions, and generating reports.
    """
import Book,Patron,Transaction
import csv
import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
        self.transactions = []
        
    def load_from_csv(self, books_file, patrons_file):
        try:
            with open(books_file, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    title, author, isbn, quantity = row
                    self.books.append(Book(title, author, isbn, int(quantity))) 
            with open(patrons_file, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, p_id, contact_info = row
                    self.patrons.append(Patron(name, int(p_id), contact_info))
        except FileNotFoundError:
            messagebox.showerror("Error", "CSV file not found.")
    
    def save_to_csv(self, books_file, patrons_file):
        with open(books_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerow([book.title, book.author, book.isbn, book.quantity])
        with open(patrons_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for patron in self.patrons:
                writer.writerow([patron.name, patron.p_id, patron.contact_info])    
                
    def add_book(self, book):
        self.books.append(book)
    def update_book(self, isbn, **kwargs):
        for book in self.books:
            if book.isbn == isbn:
                for key, value in kwargs.items():
                    setattr(book, key, value)
                return
        print("Book not found.")


    def add_patron(self, patron):
        self.patrons.append(patron)
    def update_patron(self, p_id, **kwargs): #kwargs takes any number of args and is p_identified as a dict
        for patron in self.patrons:
            if patron.p_id == p_id:
                for key, value in kwargs.items():
                    setattr(patron, key, value)
                return
        print("Patron not found.")
    def remove_patron(self, p_id):
        for i, patron in enumerate(self.patrons):
            if patron.p_id == p_id:
                del self.patrons[i]
                print("Patron removed successfully.")
                return
        print("Patron not found.")


    def check_out_book(self, patron_p_id, isbn, due_date):
        patron = self.find_patron_by_p_id(patron_p_id)
        book = self.find_book_by_isbn(isbn)
        if patron and book:
            if book.quantity > 0:
                self.transactions.append((patron, book, due_date))
                book.quantity -= 1
                print(f"{book.title} checked out to {patron.name}. Due date: {due_date}")
            else:
                print("Sorry, the book is out of stock.")
        else:
            print("Patron or book not found.")
    def check_in_book(self, patron_p_id, isbn):
        for i, (patron, book, due_date) in enumerate(self.transactions):
            if patron.p_id == patron_p_id and book.isbn == isbn:
                del self.transactions[i]
                book.quantity += 1
                print(f"{book.title} checked in from {patron.name}.")
                return
        print("Transaction not found.")
        
        
    def display_books(self):
        print("Book Report")
        for book in self.books:
            book.display()
    def display_patrons(self):
        print("Patron Report")
        for patron in self.patrons:
            patron.display()

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    def find_patron_by_p_id(self, p_id):
        for patron in self.patrons:
            if patron.p_id == p_id:
                return patron
        return None

#GUI of the library
class LibraryGUI:
    def __init__(self, root, library):
        self.root = root
        self.library = library

        # Create a menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        # Create the menu items
        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="Save", command=self.on_save)
        file_menu.add_command(label="Exit", command=self.on_exit)
        menu.add_cascade(label="File", menu=file_menu)

        # Create a frame for the book list
        self.book_listbox = tk.Listbox(self.root, width=50, height=10)
        self.book_listbox.pack()

        # Populate the book listbox
        for book in self.library.books:
            self.book_listbox.insert(tk.END, f"{book.title} - {book.author} - {book.isbn} - {book.quantity}")

        # Create a frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        # Create buttons
        add_book_button = tk.Button(button_frame, text="Add Book", command=self.on_add_book)
        add_book_button.grid(row=0, column=0, padx=5, pady=5)

        update_book_button = tk.Button(button_frame, text="Update Book", command=self.on_update_book)
        update_book_button.grid(row=0, column=1, padx=5, pady=5)

        remove_book_button = tk.Button(button_frame, text="Remove Book", command=self.on_remove_book)
        remove_book_button.grid(row=0, column=2
                            
    def on_add_book(self):
        # Implement the logic for adding a book here
        pass

    def on_update_book(self):
        # Implement the logic for updating a book here
        pass

    def on_remove_book(self):
        # Implement the logic for removing a book here
        pass

    def on_display_books(self):
        # Implement the logic for displaying books here
        pass

    def on_display_patrons(self):
        # Implement the logic for displaying patrons here
        pass

    def on_save(self):
        # Implement the logic for saving data to CSV files here
        self.library.save_to_csv('books.csv', 'patrons.csv')

    def on_exit(self):
        self.root.destroy()
