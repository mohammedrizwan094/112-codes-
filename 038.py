"""Problem 038: Check if a 3-digit number is an Armstrong number (e.g., 153)"""

n = int(input("Enter a 3-digit number: "))
if 100 <= n <= 999:
    total = sum(int(digit) ** 3 for digit in str(n))
    print("Armstrong number" if total == n else "Not an Armstrong number")
else:
    print("Please enter a 3-digit positive number")
