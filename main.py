import os
import csv
import sys
from datetime import datetime, timedelta
import Library

def create_sample_data():
    """Create sample data for books and patrons."""
    return [
        Library.Book("Book1", "Author1", "1234567890", 1),
        Library.Book("Book2", "Author2", "0987654321", 2),
    ], [
        Library.Patron("Patron1", "1234567890"),
        Library.Patron("Patron2", "0987654321"),
    ]


def write_to_csv(data: list[dict], file_name: str):
    """Write data to a CSV file."""
    fieldnames = data[0].keys()

    with open(file_name, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def main():
    # Create sample data and save it to CSV files
    books, patrons = create_sample_data()

    books_data = [vars(book) for book in books]
    write_to_csv(books_data, "books.csv")

    patrons_data = [vars(patron) for patron in patrons]
    write_to_csv(patrons_data, "patrons.csv")

    # Create transactions using the first book and patron
    transaction_data = []
    book = books[0]
    patron = patrons[0]
    transaction_date = datetime.now()

    for _ in range(5):
        Library.Transaction.create_transaction(book, patron, transaction_date)
        transaction_data.append(vars(book))
        transaction_date += timedelta(days=1)

    transactions_data = [
        {
            **transaction,
            "patron_id": transaction.patron.id,
            "transaction_date": transaction.transaction_date.strftime("%Y-%m-%d"),
        }
        for transaction in transaction_data
    ]

    write_to_csv(transactions_data, "transactions.csv")


if __name__ == "__main__":
    main()