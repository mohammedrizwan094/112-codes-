"""Problem 052: Happy Number: Repeatedly replace a number with the sum of the squares of its digits. Determine whether it eventually reaches 1."""

n = int(input("Enter a positive integer: "))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = sum(int(digit) ** 2 for digit in str(abs(n)))
print("Happy number" if n == 1 else "Not a happy number")
