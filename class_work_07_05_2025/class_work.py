import sqlite3
import os

conn = sqlite3.connect("C:\\Users\\kaarl\\Desktop\\GitHub\\python\\class_work_07_05_2025\\books.sqlite")
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Books')
cur.execute('''
    CREATE TABLE Books (
        author_first_name TEXT,
        author_last_name TEXT,
        title TEXT,
        printing_house TEXT,
        year INTEGER
    )
''')

cur.executemany('''
    INSERT INTO Books (author_first_name, author_last_name, title, printing_house, year)
    VALUES (?, ?, ?, ?, ?)
''', [
    ("John", "Doe", "Book One", "House A", 2025),
    ("Jane", "Smith", "Book Two", "House B", 2025),
    ("Alice", "Johnson", "Book Three", "House C", 2023),
    ("Bob", "Brown", "Book Four", "House D", 2024),
    ("Charlie", "Davis", "Book Five", "House E", 2022)
])

cur.execute('SELECT * FROM Books WHERE year = 2025')
books_2025 = cur.fetchall()
for book in books_2025:
    print(book)

conn.commit()
conn.close()