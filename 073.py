"""Problem 073: Read numbers until user enters −1, print the count and average"""

total = 0.0
count = 0
while True:
    number = float(input("Enter a number (-1 to stop): "))
    if number == -1:
        break
    total += number
    count += 1
print("Count:", count)
if count:
    print("Average:", total / count)
else:
    print("No numbers were entered")
