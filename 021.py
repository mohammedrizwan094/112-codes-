"""Problem 021: Ticket Pricing : Calculate ticket price based on the customer's age."""

age = int(input("Enter customer age: "))
# Example ticket pricing rules; change prices if your assignment specifies others.
if age < 5:
    price = 0
elif age <= 12:
    price = 50
elif age <= 59:
    price = 100
else:
    price = 60
print("Ticket price:", price)
