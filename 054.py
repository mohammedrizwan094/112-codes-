"""Problem 054: Extract and print each digit of a number from left to right"""

number = input("Enter an integer: ").strip()
digits = number.lstrip("-")
print("Digits from left to right:")
for digit in digits:
    print(digit, end=" ")
print()
