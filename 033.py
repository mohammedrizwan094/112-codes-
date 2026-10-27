"""Problem 033: Given 3 numbers, print them in ascending order using only if-else"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a <= b:
    if b <= c:
        first, second, third = a, b, c
    elif a <= c:
        first, second, third = a, c, b
    else:
        first, second, third = c, a, b
else:
    if a <= c:
        first, second, third = b, a, c
    elif b <= c:
        first, second, third = b, c, a
    else:
        first, second, third = c, b, a
print("Ascending order:", first, second, third)
