# Version with input validation
while True:
    try:
        hours = float(input("Enter hours: "))
        if hours < 0:
            print("Please enter a positive number.")
            continue
        break
    except:
        print("Error, please enter numeric input.")

while True:
    try:
        rate = float(input("Enter rate: "))
        if rate < 0:
            print("Please enter a positive number.")
            continue
        break
    except:
        print("Error, please enter numeric input.")

if hours > 40:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * rate * 1.75
    pay = regular_pay + overtime_pay
else:
    pay = hours * rate

print("Pay:", pay)