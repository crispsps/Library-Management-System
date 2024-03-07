"""Transaction Class
Create a Transaction class to handle book checkouts and returns.
Implement methods for checking in/out books, recording due dates, and managing fines (if applicable).
"""
from datetime import datetime, timedelta


class Transaction:
    def __init__(self, check_book, due_date=None, fine=0):
        self.check_book = check_book
        self.due_date = due_date
        self.fine = fine

    def check_out(self, patron, book, due_date):
        if book.quantity > 0:
            if patron.id not in self.checked_out_books:
                self.checked_out_books[patron.id] = []
            self.checked_out_books[patron.id].append((book, due_date))
            book.quantity -= 1
            print(f"{book.title} checked out to {patron.name}. Due date: {due_date}")
        else:
            print("Sorry, the book is out of stock.")

    def check_in(self, patron, book):
        if patron.id in self.checked_out_books:
            for i, (b, due_date) in enumerate(self.checked_out_books[patron.id]):
                if b.isbn == book.isbn:
                    del self.checked_out_books[patron.id][i]
                    book.quantity += 1
                    print(f"{book.title} checked in from {patron.name}.")
                    return
            print("Book not found in checked out books for this patron.")
        else:
            print("Patron has no checked out books.")

    def display_fine(self, due_date):
        today = datetime.today()
        if today > due_date:
            days_overdue = (today - due_date).days
            fine_amount = self.fine_per_day * days_overdue
            return fine_amount
        else:
            return 0