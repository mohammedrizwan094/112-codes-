"""Problem 075: Palindrome Check: Check whether a string is a palindrome using recursion"""

def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

word = input("Enter a string: ")
print("Palindrome" if is_palindrome(word) else "Not a palindrome")
