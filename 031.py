"""Problem 031: Read month number (1–12) and print number of days in that month"""

month = int(input("Enter month number (1-12): "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= month <= 12:
    print("Number of days:", days_in_month[month - 1])
    if month == 2:
        print("February has 29 days in a leap year.")
else:
    print("Invalid month")
