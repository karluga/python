# how many different cereal names come from each manufacturer?
# Task 5.1 using dictionary

import re

file_name = "cereals.csv"
counts = {} # Empty dictionary
with open(file_name) as file:
    next(file) # Skip first line
    for line in file:
        # Split line by commas not inside quotes
        row = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line.strip())
        manufacturer = row[1]  # Manufacturer column
        counts[manufacturer] = counts.get(manufacturer, 0) + 1

print(counts)

# Sort dictionary by Manufacturer name and print
print("SORTED:")
for key in sorted(counts):
    print(f"{key}: {counts[key]}")
