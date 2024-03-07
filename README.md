# Library-Management-System 
A comprehensive Library Management System using Python that allows librarians to manage books, patrons, and transactions efficiently. The system should provide functionalities such as adding and removing books, checking in/out books, managing patrons, and generating reports.

Structure:

Book Class
Represents each book with attributes: title, author, ISBN, quantity
Adds books with add_book(book) method.
Updates books with update_book(isbn, **kwargs)
Removes books with remove_book(isbn)
Displays book details with display()\

Patron Class
Represents library patrons with attributes like name, ID, contact information
Adds patrons with add_patron(patron) method.
Updates patrons with update_patron(p_id, **kwargs) method.
Removes patrons with remove_patron(p_id) method.
Displays patron details with display() method.

Transaction Class
Handles book checkouts and returns.
Checks out books with check_out_book(patron_p_id, isbn, due_date) method.
Checks in books with check_in_book(patron_p_id, isbn) method.

Library Class
Manages the overall library system.
Includes methods for searching books, managing patrons, handling transactions, and generating reports.

Database Integration
Implements data storage using CSV to store book and patron information with pandas to read csv files.

User Interface
Develops a simple GUI to interact with the LMS using tkinter.

How to use:
Run the run.py file in an editor to view a table of information for both books and patrons.

