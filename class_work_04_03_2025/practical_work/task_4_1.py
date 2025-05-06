# which email addresses sent messages, and how many lines start with "From"?
# task 4.1 using lists

filename = "mbox-short.txt"

with open(filename, 'r') as f:
    email_list = []
    count = 0
    for line in f:
        if line.startswith("From "):  # Only process lines that start with "From "
            words = line.split()
            if len(words) > 1:
                email_list.append(words[1])  # Extract the email address
                count += 1

    # Sort emails alphabetically and print them
    for email in sorted(email_list):
        print(email)

    # Print the count of "From " lines
    print(f"There were {count} lines in the file with From as the first word")

