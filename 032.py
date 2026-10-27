"""Problem 032: Check if a number is positive, negative, or zero — then if positive check even/odd"""

n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
    print("Even" if n % 2 == 0 else "Odd")
elif n < 0:
    print("Negative")
else:
    print("Zero")
