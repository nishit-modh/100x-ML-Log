"""
4. The ATM Logic
Take balance and withdrawal_amount.
If amount > balance: Print "Insufficient Funds".
If amount is not a multiple of 100: Print "Please enter amount in multiples of 100".
If amount <= balance and valid: Subtract amount and print "Remaining Balance: [value]".
"""
balance = int(input("Enter balance: "))
to_withdraw = int(input("Enter amount you want to withdraw: "))
if to_withdraw > balance: 
    print("insufficient balance")
elif (to_withdraw%100) != 0:
    print("Enter amount in multiple of 100!")
else:
    print(f"Rs.{to_withdraw} withdrawn! Remaning balance = {balance - to_withdraw}")