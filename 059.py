"""Problem 059: Find LCM of two numbers"""

import math
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
if a == 0 or b == 0:
    print("LCM: 0")
else:
    print("LCM:", abs(a * b) // math.gcd(a, b))
