"""Problem 027: Calculate electricity bill based on slab rates"""

units = float(input("Enter electricity units used: "))
# Example slab rates: first 100 at 1.5, next 100 at 2.5, above 200 at 4.0.
if units < 0:
    print("Units cannot be negative")
else:
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    else:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4.0
    print("Electricity bill:", bill)
