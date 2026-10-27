"""Problem 020: Check if a character is a vowel or consonant"""

ch = input("Enter one alphabet: ").lower()
if len(ch) == 1 and ch.isalpha():
    print("Vowel" if ch in "aeiou" else "Consonant")
else:
    print("Please enter one alphabet")
