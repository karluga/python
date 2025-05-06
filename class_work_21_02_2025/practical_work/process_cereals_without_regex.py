def process_cereals(filename):
    with open(filename, 'r') as file:
        headers = file.readline() # Read headers
        data = file.readlines() # Read remaining lines

    cereals_data = {"C": [], "H": []}  # C for Cold, H for Hot

    for line in data:
        parts = line.split(',')

        # Check if the length of parts matches the expected number of columns
        if len(parts) == 16:
            name = parts[0]
            cereal_type = parts[2]
            rating = parts[15]

            # Filter by cereal type (C or H) and add rating
            if cereal_type in cereals_data:
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
