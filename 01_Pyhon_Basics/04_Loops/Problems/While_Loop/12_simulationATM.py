# 12. THE ATM SIMULATOR (BANKING SIMULATION)
# Start with balance = 1000. Use a while loop to show a menu: 
# 1. Deposit, 2. Withdraw, 3. Check Balance, 4. Exit.
# Prevent withdrawals that exceed the balance and loop until 'Exit' is chosen.

# Assumption : User can enter positive numbers only
balance = 1000
while True:
    print("1. Deposit, 2. Withdraw, 3. Check Balance, 4. Exit.") 
    selected = int(input("Enter a Valid Input: "))
    if selected == 1:
        deposit = int(input("Deposit amount: "))
        balance += deposit
        print(f"{deposit} is credited, New balance: {balance}")
    elif selected == 2:
        withdraw = int(input("withdraw amount: "))
        if withdraw <= balance:
            balance -= withdraw
            print(f"{withdraw} is debited, New balance: {balance}")
        else:
            print("Insufficient Balance!!!")
    elif selected == 3:
        print(f"Account balance: {balance}")
    elif selected == 4:
        break
    else:
        print("Select a valid Input")
    # for better spacing
    print()