# how many emails were received from each domain? Visualize with histogram using asterisks*.
# task 4.2 using dictionaries

filename = "mbox-short.txt"

with open(filename, 'r') as f:
    domain_count = {}

    for line in f:
        if line.startswith("From "):  # Only lines that start with "From "
            words = line.split()
            if len(words) > 1:
                email = words[1]
                domain = email.split('@')[-1]  # Extract the domain part
                domain_count[domain] = domain_count.get(domain, 0) + 1

    # Print the dictionary
    print(domain_count)

    # Sort dictionary by domain name and print formatted output
    print("\nSORTED:")
    for domain in sorted(domain_count):
        print(f"{domain:>20}: {domain_count[domain]} {'*' * domain_count[domain]}")

