"""Problem 077: Increasing + Decreasing: Using a single recursive function, print numbers in increasing order and then decreasing order."""

def print_increasing_decreasing(n, current=1):
    if current > n:
        return
    print(current, end=" ")
    print_increasing_decreasing(n, current + 1)
    print(current, end=" ")

n = int(input("Enter N: "))
print_increasing_decreasing(n)
print()
