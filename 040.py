"""Problem 040: ATM Withdrawal : Approve or reject a withdrawal based on amount, balance, and minimum-balance rules."""

balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
minimum_balance = float(input("Enter required minimum balance: "))
if amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Withdrawal rejected: insufficient balance")
elif balance - amount < minimum_balance:
    print("Withdrawal rejected: minimum balance must be maintained")
else:
    print("Withdrawal approved")
    print("Remaining balance:", balance - amount)
