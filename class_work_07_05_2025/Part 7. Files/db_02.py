import sqlite3
import os

# Use a relative path
db_path = os.path.join(os.getcwd(), "music.sqlite")
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
    ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
    ('My Way', 15))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
     print(row)

# cur.execute('DELETE FROM Tracks WHERE plays < 100')
# conn.commit()

cur.close()
