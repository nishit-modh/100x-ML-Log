# You have a price = 5000. Apply a 10% discount using *=. Then, apply a tax of 18% on the new price using *=.
price = float(input("Enter product price: "))
discount = int(input("Enter available Discount: "))
tax = int(input("Enter tax rate: "))
price *= 1 - discount / 100
price *= 1 + tax / 100
print("Final payable amount: ", price)
