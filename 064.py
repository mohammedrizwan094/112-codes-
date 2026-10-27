"""Problem 064: Compute: 1! + 2! + 3! + ... + N!"""

n = int(input("Enter N: "))
factorial = 1
total = 0
for i in range(1, n + 1):
    factorial *= i
    total += factorial
print("Sum of factorials:", total)
