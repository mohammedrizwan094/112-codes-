"""Problem 069: Print all factors / divisors of a number"""

n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Enter a positive integer")
else:
    print("Factors:", end=" ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()
