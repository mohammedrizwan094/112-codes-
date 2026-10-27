"""Problem 047: Calculate the sum of first N natural numbers"""

n = int(input("Enter N: "))
print("Sum:", n * (n + 1) // 2 if n >= 0 else "N must be non-negative")
