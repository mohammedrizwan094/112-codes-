"""Problem 015: Count the number of set bits in a number"""

n = int(input("Enter a non-negative integer: "))
count = 0
while n > 0:
    count += n & 1
    n >>= 1
print("Number of set bits:", count)
