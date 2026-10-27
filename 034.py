"""Problem 034: Find the roots of a quadratic equation (check discriminant: real, equal, imaginary)"""

import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
if a == 0:
    if b != 0:
        print("Linear equation root:", -c / b)
    else:
        print("Not a quadratic equation")
else:
    d = b * b - 4 * a * c
    if d > 0:
        print("Two real roots:", (-b + math.sqrt(d)) / (2 * a), "and", (-b - math.sqrt(d)) / (2 * a))
    elif d == 0:
        print("Equal real roots:", -b / (2 * a))
    else:
        real = -b / (2 * a)
        imaginary = math.sqrt(-d) / (2 * a)
        print("Imaginary roots:", complex(real, imaginary), "and", complex(real, -imaginary))
