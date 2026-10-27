"""Problem 022: Age Category : Classify a person as a child, teenager, adult, or senior based on age."""

age = int(input("Enter age: "))
if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")
