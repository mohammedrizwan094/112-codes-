"""Problem 067: Check if a number is an Armstrong number (generalized for any digits)"""

n = int(input("Enter a non-negative integer: "))
digits = str(abs(n))
power = len(digits)
total = sum(int(digit) ** power for digit in digits)
print("Armstrong number" if total == n else "Not an Armstrong number")
