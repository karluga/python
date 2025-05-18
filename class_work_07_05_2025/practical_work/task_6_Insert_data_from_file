# The database consists of three tables:
#
# Table: Domain
# | Column Name   | Data Type | Constraints                                  |
# |---------------|-----------|----------------------------------------------|
# | ID            | INTEGER   | NOT NULL, UNIQUE, PRIMARY KEY, AUTOINCREMENT |
# | Domain_Name   | TEXT      | NOT NULL, UNIQUE                             |
#
# Table: Emails
# | Column Name   | Data Type | Constraints                                  |
# |---------------|-----------|----------------------------------------------|
# | ID            | INTEGER   | NOT NULL, UNIQUE, PRIMARY KEY, AUTOINCREMENT |
# | Email_name    | TEXT      | NOT NULL, UNIQUE                             |
# | Domain_ID     | INTEGER   | NOT NULL, FOREIGN KEY REFERENCES Domain(ID)  |
#
# Table: Messages
# | Column Name     | Data Type | Constraints                                  |
# |-----------------|-----------|----------------------------------------------|
# | ID              | INTEGER   | NOT NULL, UNIQUE, PRIMARY KEY, AUTOINCREMENT |
# | Email_ID        | INTEGER   | NOT NULL, FOREIGN KEY REFERENCES Emails(ID)  |
# | Subject         | TEXT      |                                              |
# | Message         | TEXT      |                                              |
# | Weekday         | TEXT      | NOT NULL                                     |
# | Spam_Confidence | REAL      |                                              |

# No duplicates!
# Tasks:
# 1. Emails recieved from one domain (user writes - gmail.com)
# 2. Only those e-mails received on Fridays and Saturdays
# 3. displaying (printing out) data nicely formatted with indentations in 4 columns:
# • Day of the week,
# • Domain name,
# • E-mail address,
# • Spam confidence level.


import sqlite3

conn = sqlite3.connect("C:\\Users\\kaarl\\Desktop\\GitHub\\python\\class_work_07_05_2025\\practical_work\\emails.sqlite")
cur = conn.cursor()

filename = "C:\\Users\\kaarl\\Desktop\\GitHub\\python\\class_work_07_05_2025\\practical_work\\mbox.txt"

with open(filename, 'r') as f:
    emails = []
    domains = []
    messages = []
    current_email = None
    current_subject = None
    current_text = None
    current_weekday = None
    current_spam_confidence = None

    for line in f:
        if line.startswith("From "):  # Extract email address, domain, and weekday
            if current_text is not None:  # Save the previous message before starting a new one
                if current_subject and current_text:
                    messages.append((current_subject, "\n".join(current_text), current_weekday, current_spam_confidence))
                current_subject = current_text = current_weekday = current_spam_confidence = None
            words = line.split()
            if len(words) > 2:
                email = words[1]
                current_email = email.split('@')[0]
                domain = email.split('@')[-1]
                current_weekday = words[2]
                domains.append(domain)
                emails.append(current_email)
        elif line.startswith("Subject:"):
            current_subject = line[len("Subject: "):].strip()
        elif line.startswith("X-DSPAM-Confidence:"):
            current_spam_confidence = float(line[len("X-DSPAM-Confidence: "):].strip())
        elif line.startswith("X-DSPAM-Probability:"):
            current_text = []
        elif current_text is not None:  # Collect email text until the next "From " block
            current_text.append(line.strip())

# Domains
unique_domains = list(set(domains))
print(unique_domains)
domain_id_map = {}
for idx, domain in enumerate(unique_domains, start=1):
    domain_id_map[domain] = idx
    cur.execute('INSERT INTO Domain (ID, Domain_Name) VALUES (?, ?)', (idx, domain))

# Emails
print(emails)
unique_emails = list(set(emails))
print(unique_emails)
email_id_map = {}
for idx, email in enumerate(unique_emails, start=1):
    domain = domains[emails.index(email)]  # Get the domain for the email
    domain_id = domain_id_map[domain]
    email_id_map[email] = idx
    cur.execute('INSERT INTO Emails (ID, Email_name, Domain_ID) VALUES (?, ?, ?)', (idx, email, domain_id))

# Messages
for idx, (subject, text, weekday, spam_confidence) in enumerate(messages, start=1):
    email_id = email_id_map.get(emails[idx - 1])
    cur.execute('INSERT INTO Messages (ID, Email_ID, Subject, Message, Weekday, Spam_Confidence) VALUES (?, ?, ?, ?, ?, ?)',
                (idx, email_id, subject, text, weekday, spam_confidence))
print(messages)
conn.commit()
conn.close()
