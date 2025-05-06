# display the average cups per serving and average calories per serving for each manufacturer
# Task 5.2 using tuples

import re

file_name = "cereals.csv"
averages = {}
cups_data = {}
calories_data = {}

with open(file_name) as file:
    next(file)  # Skip first line
    for line in file:
        # Split line by commas not inside quotes
        row = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line.strip())

        manufacturer = row[1]
        try:
            cups = float(row[8])  # Cups per serving column
            calories = int(row[3])  # Calories column
        except ValueError:
            continue  # Skip rows with invalid numeric data
        
        if manufacturer not in averages:
            cups_data[manufacturer] = []
            calories_data[manufacturer] = []
        
        cups_data[manufacturer].append(cups)
        calories_data[manufacturer].append(calories)

# Compute averages
average_list = []
for manufacturer in cups_data:
    avg_cups = sum(cups_data[manufacturer]) / len(cups_data[manufacturer])
    avg_calories = sum(calories_data[manufacturer]) / len(calories_data[manufacturer])
    average_list.append((manufacturer, round(avg_cups, 1), round(avg_calories)))

# Print list of tuples
print(average_list)

# Sort by average Calories per serving
print("SORTED:")
print("Manufacturer: Cups: Calories:")
for manufacturer, avg_cups, avg_calories in sorted(average_list, key=lambda x: x[2]):
    print(f"{manufacturer}: {avg_cups} {avg_calories}")