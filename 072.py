"""Problem 072: Convert binary to decimal"""

binary = input("Enter a binary number: ").strip()
if binary and all(bit in "01" for bit in binary):
    decimal = 0
    for bit in binary:
        decimal = decimal * 2 + int(bit)
    print("Decimal:", decimal)
else:
    print("Invalid binary number")
