import sqlite3
import os

# Use a relative path
# conn = sqlite3.connect("C:\\Users\\kaarl\\Desktop\\GitHub\\python\\class_work_07_05_2025\\Part 7. Files\\music.sqlite")
db_path = os.path.join(os.getcwd(), "music.sqlite")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()