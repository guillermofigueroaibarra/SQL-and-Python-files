'''

Name: Guillermo Figueroa
Date: 12/10/2021
Program Description: this program shows us how to select data from file by using SQL and python. 


'''


import sqlite3


connection = sqlite3.connect('books.db') # connect to database and get connection object





# use SWL query and pandas to view the authors table's contents


import pandas as pd

pd.options.display.max_columns = 10 

displayResults = pd.read_sql('SELECT * FROM authors', connection, index_col=['id']) 


print(displayResults)
print()


# USE SQL and pandas to view the titles table's contents

viewTitles = pd.read_sql('SELECT * FROM titles', connection) # view the titles table's contents
print(viewTitles)
print()



df = pd.read_sql('SELECT * FROM author_ISBN', connection) # display the authors ids and isbn
print(df.head())
print()




predicateRows = pd.read_sql("""SELECT title, edition, copyright FROM titles WHERE copyright > '2016'""", connection) # select title, edition and copyright for all books
print(predicateRows)
print()




authorsD = pd.read_sql("""SELECT id, first, last FROM authors WHERE last LIKE 'D%'""", # locate all authors who's last name starts with letter D
            connection, index_col=['id'])
print(authorsD)
print()



authorsB = pd.read_sql("""SELECT id, first, last FROM authors WHERE first LIKE '_b%'""", # select all authors whose last names start with anny character followed by the letter b
            connection, index_col=['id'])
print(authorsB)
print()



titlesAscending = pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection) # sort titles in ascending order
print(titlesAscending)
print()



authorsByLastFirst = pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last, first""",
            connection, index_col=['id']) # sort authors name by last name then by first name
print(authorsByLastFirst)


authorsLastAsc = pd.read_sql("""SELECT id, first, last FROM authors ORDER BY last DESC, first ASC""",
            connection, index_col=['id']) # select authors in descending order by last name and ascending order by first name if authors have the same last name
print(authorsLastAsc)
print()


titleEndingIn = pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title""", connection) # select books whose title ends with 'how to program'
print(titleEndingIn)
print()

mergeMultipleTables = pd.read_sql("""SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first""", connection).head() # merge data from multiple tables
print(mergeMultipleTables)
print()

cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last) VALUES ('Sue', 'Red')""") # insert new author

authorsTable = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])
print(authorsTable)
print()


cursor = cursor.execute("""UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue'""")

authTable = pd.read_sql("SELECT id, first, last FROM authors", connection, index_col=['id'])
print(authTable)
print()


cursor = cursor.execute('DELETE FROM authors WHERE id=6')



authorsDelete = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id']) # WHERE is omitted, all the table's rows are deleted
print(authorsDelete)
print()


editionNum = pd.read_sql("""SELECT title, edition FROM titles ORDER BY edition DESC""", connection).head(3) # select titles table all the titles and their edition numbers in descending order by edition number
print(editionNum)
print()


firstA = pd.read_sql("""SELECT * FROM authors WHERE first LIKE 'A%'""", connection) # select authors whose first name starts with A
print(firstA)
print()


doNotEnd = pd.read_sql("""SELECT isbn, title, edition, copyright FROM titles WHERE title NOT LIKE '%How to Program' ORDER BY title""", connection) #titles that don't end in 'how to program'
print(doNotEnd)
print()



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
= RESTART: C:/Users/guill/Documents/SCHOOL FALL 2021/ADVANCED PYTHON/Week 12/exercise-17.2.py
        first    last
id                   
1        Paul  Deitel
2      Harvey  Deitel
3       Abbey  Deitel
4         Dan   Quirk
5   Alexander    Wald

         isbn                             title  edition copyright
0  0135404673     Intro to Python for CS and DS        1      2020
1  0132151006     Internet & WWW How to Program        5      2012
2  0134743350               Java How to Program       11      2018
3  0133976890                  C How to Program        8      2016
4  0133406954  Visual Basic 2012 How to Program        6      2014
5  0134601548          Visual C# How to Program        6      2017
6  0136151574         Visual C++ How to Program        2      2008
7  0134448235                C++ How to Program       10      2017
8  0134444302            Android How to Program        3      2017
9  0134289366         Android 6 for Programmers        3      2016

   id        isbn
0   1  0134289366
1   2  0134289366
2   5  0134289366
3   1  0135404673
4   2  0135404673

                           title  edition copyright
0  Intro to Python for CS and DS        1      2020
1            Java How to Program       11      2018
2       Visual C# How to Program        6      2017
3             C++ How to Program       10      2017
4         Android How to Program        3      2017

     first    last
id                
1     Paul  Deitel
2   Harvey  Deitel
3    Abbey  Deitel

    first    last
id               
3   Abbey  Deitel

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

        first    last
id                   
3       Abbey  Deitel
2      Harvey  Deitel
1        Paul  Deitel
4         Dan   Quirk
5   Alexander    Wald
        first    last
id                   
5   Alexander    Wald
4         Dan   Quirk
3       Abbey  Deitel
2      Harvey  Deitel
1        Paul  Deitel

         isbn                             title  edition copyright
0  0134444302            Android How to Program        3      2017
1  0133976890                  C How to Program        8      2016
2  0134448235                C++ How to Program       10      2017
3  0132151006     Internet & WWW How to Program        5      2012
4  0134743350               Java How to Program       11      2018
5  0133406954  Visual Basic 2012 How to Program        6      2014
6  0134601548          Visual C# How to Program        6      2017
7  0136151574         Visual C++ How to Program        2      2008

    first    last        isbn
0   Abbey  Deitel  0132151006
1   Abbey  Deitel  0133406954
2  Harvey  Deitel  0134289366
3  Harvey  Deitel  0135404673
4  Harvey  Deitel  0132151006

        first    last
id                   
1        Paul  Deitel
2      Harvey  Deitel
3       Abbey  Deitel
4         Dan   Quirk
5   Alexander    Wald
6         Sue     Red

        first    last
id                   
1        Paul  Deitel
2      Harvey  Deitel
3       Abbey  Deitel
4         Dan   Quirk
5   Alexander    Wald
6         Sue   Black

        first    last
id                   
1        Paul  Deitel
2      Harvey  Deitel
3       Abbey  Deitel
4         Dan   Quirk
5   Alexander    Wald

                 title  edition
0  Java How to Program       11
1   C++ How to Program       10
2     C How to Program        8

   id      first    last
0   3      Abbey  Deitel
1   5  Alexander    Wald

         isbn                          title  edition copyright
0  0134289366      Android 6 for Programmers        3      2016
1  0135404673  Intro to Python for CS and DS        1      2020

>>>

'''
