"""Problem 055: Find factorial of N"""

n = int(input("Enter N: "))
if n < 0:
    print("Factorial is not defined for negative integers")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial:", factorial)
