"""Problem 014: Check if the Kth bit of a number is set or not"""

n = int(input("Enter a non-negative integer: "))
k = int(input("Enter bit position K (starting from 0): "))
if k < 0 or n < 0:
    print("Enter non-negative values")
elif n & (1 << k):
    print("The Kth bit is set")
else:
    print("The Kth bit is not set")
