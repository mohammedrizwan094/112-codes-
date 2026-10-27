"""Problem 048: Count the number of digits in a number"""

n = abs(int(input("Enter an integer: ")))
count = 1 if n == 0 else 0
while n > 0:
    count += 1
    n //= 10
print("Number of digits:", count)
