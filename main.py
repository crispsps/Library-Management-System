import csv
import pandas as pd

"""File for reading csv files"""

#Using csv
# with (open('books.csv', 'r')) as books_file:
#     reader = csv.reader(books_file)
#     for row in reader:
#         print(row)
        
# with (open('patrons.csv', 'r')) as p_file:
#     reader = csv.reader(p_file)
#     for row in reader:
#         print(row)
        
#using pandas
books_df = pd.read_csv('books.csv')

# Print the books.csv data
print("Books:")
print(books_df)

# Read the patrons.csv file
patrons_df = pd.read_csv('patrons.csv')

# Print the patrons.csv data
print("\nPatrons:")
print(patrons_df)