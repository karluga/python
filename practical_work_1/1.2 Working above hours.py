# Version with Overtime
hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
if hours > 40:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * rate * 1.75
    pay = regular_pay + overtime_pay
else:
    pay = hours * rate
print("Pay:", pay)