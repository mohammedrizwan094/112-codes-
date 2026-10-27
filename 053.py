"""Problem 053: Product of Digits: Find the product of all digits of a number using recursion."""

def product_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) * product_of_digits(n // 10)

number = int(input("Enter an integer: "))
print("Product of digits:", product_of_digits(number))
