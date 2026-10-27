"""Problem 026: Read a number (1–7) and print the corresponding day of the week"""

day = int(input("Enter day number (1-7): "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if 1 <= day <= 7:
    print(days[day - 1])
else:
    print("Invalid day number")
