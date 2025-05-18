import sqlite3

conn = sqlite3.connect("C:\\Users\\kaarl\\Desktop\\GitHub\\python\\class_work_07_05_2025\\practical_work\\emails.sqlite")
cur = conn.cursor()

weekday_mapping = {
    "Fri": "Friday",
    "Sat": "Saturday"
}

domain_to_search = input("Enter the domain to search: ").strip()

query = """
SELECT Messages.Weekday, Domain.Domain_Name, Emails.Email_name, Messages.Spam_Confidence
FROM Messages
JOIN Emails ON Messages.Email_ID = Emails.ID
JOIN Domain ON Emails.Domain_ID = Domain.ID
WHERE (Messages.Weekday = 'Fri' OR Messages.Weekday = 'Sat')
  AND Domain.Domain_Name = ?
ORDER BY Messages.Weekday, Domain.Domain_Name, Emails.Email_name;
"""

cur.execute(query, (domain_to_search,))
rows = cur.fetchall()

current_weekday = None
current_domain = None

for row in rows:
    weekday, domain, email, spam_confidence = row
    full_weekday = weekday_mapping.get(weekday, weekday)  # Map abbreviation to full name
    
    if full_weekday != current_weekday:
        current_weekday = full_weekday
        current_domain = None
        print(full_weekday)
    if domain != current_domain:
        current_domain = domain
        print(f"    {domain}")
    print(f"        {email}@{domain}")
    print(f"            spam confidence: {spam_confidence}")

conn.close()

