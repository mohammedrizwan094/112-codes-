"""Problem 071: Convert decimal to binary"""

n = int(input("Enter a non-negative decimal integer: "))
if n < 0:
    print("Enter a non-negative integer")
elif n == 0:
    print("Binary: 0")
else:
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    print("Binary:", binary)
