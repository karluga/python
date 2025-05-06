def read_cereals(file_name):
    with open(file_name, 'r') as file:
        content = file.read().strip().split('\n')
        for line in content[1:]:
            parts = line.split(',')
            print(f"{parts[1]}: {parts[0]}")

# Usage
file_name = input("Enter a file name: ")
file_name = "C:\\Users\\kaarl\\Desktop\\GitHub\\python-practice\\class_work_21_02_2025\\" + file_name
read_cereals(file_name)
