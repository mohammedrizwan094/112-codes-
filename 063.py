"""Problem 063: Find x^n (power) without using built-in pow function"""

x = float(input("Enter x: "))
n = int(input("Enter non-negative exponent n: "))
if n < 0:
    print("Please enter a non-negative exponent")
else:
    result = 1
    for _ in range(n):
        result *= x
    print("x^n =", result)
