import sqlite3

conn = sqlite3.connect("C:\\Users\\kaarl\\Desktop\\GitHub\\python\\class_work_07_05_2025\\practical_work\\emails.sqlite")
cur = conn.cursor()

cur.execute("""CREATE TABLE "Domain" (
    "ID"    INTEGER NOT NULL UNIQUE,
    "Domain_Name"    TEXT NOT NULL UNIQUE,
    PRIMARY KEY("ID" AUTOINCREMENT)
);""")

cur.execute("""CREATE TABLE Emails (
    ID    INTEGER NOT NULL UNIQUE,
    Email_name    TEXT NOT NULL UNIQUE,
    Domain_ID    INTEGER NOT NULL,
    PRIMARY KEY(ID AUTOINCREMENT),
    FOREIGN KEY(Domain_ID) REFERENCES Domain(ID)
);""")

cur.execute("""CREATE TABLE "Messages" (
    "ID"    INTEGER NOT NULL UNIQUE,
    "Email_ID"    INTEGER NOT NULL,
    "Subject"    TEXT,
    "Message"    TEXT,
    "Weekday"    TEXT NOT NULL,
    "Spam_Confidence"    REAL,
    PRIMARY KEY("ID" AUTOINCREMENT),
    FOREIGN KEY("Email_ID") REFERENCES "Emails"("ID")
);""")

conn.commit()
cur.close()