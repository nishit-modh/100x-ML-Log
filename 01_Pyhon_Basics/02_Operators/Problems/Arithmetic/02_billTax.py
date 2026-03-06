#Total bill amout with tax(GST)
price = float(input("Enter product price: "))
quantity = float(input("Enetr product quantity: "))
total_price = price*quantity
final_price = total_price*1.18
print(f"Price before tax: {total_price} | Price after tax: {final_price}")
print(f"Tax paid: {total_price * .18}")