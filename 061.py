"""Problem 061: Compute the sum: 1 + 1/2 + 1/3 + ... + 1/N"""

n = int(input("Enter N: "))
total = 0.0
for i in range(1, n + 1):
    total += 1 / i
print("Series sum:", total)
