"""Problem 039: Given hours worked and rate, compute salary with overtime (>40 hrs at 1.5× rate)"""

hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
if hours < 0 or rate < 0:
    print("Hours and rate cannot be negative")
elif hours > 40:
    salary = 40 * rate + (hours - 40) * rate * 1.5
    print("Salary:", salary)
else:
    print("Salary:", hours * rate)
