import re # regex library

def process_cereals(filename):
    with open(filename, 'r') as file:
        headers = file.readline()  # Read headers
        data = file.readlines() # Read remaining lines

    pattern = re.compile(r'''
        ([^,]*),       # Capture name
        [^,]*,         # Skip manufacturer
        ([CH]),        # Capture type ('C' or 'H')
        (?:[^,]*,){12} # Skip 12 fields
        ([^,]*)        # Capture rating
    ''', re.VERBOSE)
    
    cereals_data = {"C": [], "H": []}  # C for Cold, H for Hot

    for line in data:
        match = pattern.match(line)
        if match:
            # Define column names for each group
            name, cereal_type, rating = match.groups()
            try:
                cereals_data[cereal_type].append((float(rating), name))
            except:
                continue # Skip invalid rows

    for cereal_type, cereals in cereals_data.items():
        if cereals:
            cereals.sort()
            min_rating, min_cereal = cereals[0]
            max_rating, max_cereal = cereals[-1]
            avg_rating = sum(r[0] for r in cereals) / len(cereals)
            
            print(f"Cereal type: {'Hot' if cereal_type == 'H' else 'Cold'}")
            print(f"The lowest cereals rating value: {min_rating} Cereal name: {min_cereal}")
            print(f"The average cereals rating value: {avg_rating}")
            print(f"The highest cereals rating value: {max_rating} Cereal name: {max_cereal}\n")

process_cereals("cereals.csv")
