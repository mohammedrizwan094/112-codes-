"""Problem 036: Read the cost price and selling price — print profit, loss, or no profit no loss"""

cost = float(input("Enter cost price: "))
selling = float(input("Enter selling price: "))
if selling > cost:
    print("Profit:", selling - cost)
elif selling < cost:
    print("Loss:", cost - selling)
else:
    print("No profit, no loss")
