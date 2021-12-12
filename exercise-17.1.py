'''

Name: Guillermo Figueroa
Date: 12/10/2021
Program Description: this program uses sql to select information from a database with certain conditions and filters


'''



import sqlite3

connection = sqlite3.connect('books.db') # connect to the database

import pandas as pd


# A)
authorsLastDescen = pd.read_sql("""SELECT last FROM authors ORDER BY last DESC""", connection) # select all authors last name from the authors table in descending order
print(authorsLastDescen)
print()


# B)
bookTitlesAscending = pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
print(bookTitlesAscending)
print()


###C)
##specificAuthorBooks = pd.read_sql("""SELECT title, copyright, year, isbn
##                                    FROM authors
##                                    INNER JOIN books
##                                    WHERE first == '%Abbey'
##                                    ORDER BY title""", connection).head()
##
##print(specificAuthorBooks)
##print()
##


# D)
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Guillermo', 'Figueroa')""") #insert Guillermo Figueroa as a new author
mergeNewAuthor = pd.read_sql("SELECT id, first, last FROM authors", connection, index_col=['id'])
print(mergeNewAuthor)
print()



### E)
##cursor = connection.cursor()
##cursor = cursor.execute("""INSERT INTO authors (titles, isbn) VALUES ('Python Basics Book', '092093034')""") # insert python Basics book as a new book
##
##


'''

OUTPUT

>>> 
= RESTART: C:/Users/guill/Documents/SCHOOL FALL 2021/ADVANCED PYTHON/Week 12/exercise-17.1.py
     last
0    Wald
1   Quirk
2  Deitel
3  Deitel
4  Deitel

                              title
0         Android 6 for Programmers
1            Android How to Program
2                  C How to Program
3                C++ How to Program
4     Internet & WWW How to Program
5     Intro to Python for CS and DS
6               Java How to Program
7  Visual Basic 2012 How to Program
8          Visual C# How to Program
9         Visual C++ How to Program

        first      last
id                     
1        Paul    Deitel
2      Harvey    Deitel
3       Abbey    Deitel
4         Dan     Quirk
5   Alexander      Wald
6   Guillermo  Figueroa

>>> 
