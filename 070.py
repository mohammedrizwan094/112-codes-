"""Problem 070: Check if a number is a perfect number (sum of divisors == number)"""

n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Enter a positive integer")
else:
    total = sum(i for i in range(1, n) if n % i == 0)
    print("Perfect number" if total == n else "Not a perfect number")
