"""Problem 068: Find the largest and smallest digit in a number"""

n = input("Enter an integer: ").strip().lstrip("-")
if n:
    digits = [int(digit) for digit in n]
    print("Largest digit:", max(digits))
    print("Smallest digit:", min(digits))
else:
    print("No digits entered")
