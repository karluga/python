# what is the frequency of each letter (a-z) in two different language texts, and how do they compare?
# task 4.3 using a list of tuples

def letter_frequency(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read().lower()  # Convert text to lowercase
        
    letter_counts = {}
    for char in text:
        if 'a' <= char <= 'z':  # Count only a-z
            letter_counts[char] = letter_counts.get(char, 0) + 1

    total_letters = sum(letter_counts.values())

    # Convert to percentage and sort by frequency
    letter_freq = [(char, round(count / total_letters * 100, 1)) for char, count in letter_counts.items()]
    letter_freq.sort(key=lambda x: x[1], reverse=True)  # Sort by frequency

    return letter_freq

files = [
    "text_LV.txt",
    "text_EN.txt"
]

# Get frequencies for each file
frequencies = [letter_frequency(file) for file in files]

# Print results in parallel columns
print(f"\n{'Latvian:':<12} {'English:':<12}")
for i in range(max(len(frequencies[0]), len(frequencies[1]))):
    latvian_data = f"{frequencies[0][i][0]}: {frequencies[0][i][1]}%" if i < len(frequencies[0]) else " "
    english_data = f"{frequencies[1][i][0]}: {frequencies[1][i][1]}%" if i < len(frequencies[1]) else " "
    print(f"{latvian_data:<12} {english_data:<12}")