"""Problem 051: Check if a number is a palindrome"""

n = input("Enter an integer: ")
print("Palindrome" if n == n[::-1] else "Not a palindrome")
