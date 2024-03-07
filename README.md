# Library-Management-System 
A comprehensive Library Management System using Python that allows librarians to manage books, patrons, and transactions efficiently. The system should provide functionalities such as adding and removing books, checking in/out books, managing patrons, and generating reports.

Implemented using csv file system and tkinter GUI.

Structure:
Book Class
Represents each book with attributes like title, author, ISBN, quantity, etc.
Adds books with add_book(book) method.
Updates books with update_book(isbn, **kwargs) method.
Removes books with remove_book(isbn) method.
Displays book details with display() method.\

Patron Class
Represents library patrons with attributes like name, ID, contact information, etc.
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

How to use:
