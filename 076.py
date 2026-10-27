"""Problem 076: Count Vowels: Count the number of vowels in a string using recursion."""

def count_vowels(text):
    if not text:
        return 0
    first = 1 if text[0].lower() in "aeiou" else 0
    return first + count_vowels(text[1:])

text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
