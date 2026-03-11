# 9. THE SECURITY LOCKOUT SYSTEM
# An outer loop allows for 3 "System Login" attempts.
# An inner loop asks the user to enter a 4-digit PIN one digit at a time.
# If a digit is non-numeric, use 'continue' to ask for that digit again.
# If the PIN is correct, break both loops. 
# If 3 attempts fail, print "System Locked".

pin = "1234"
for i in range(1, 4):
    user_pin = ""
    j = 1
    while j < 5 :
        digit = input(f"Enter no.{j} digit of your pin: ")
        # to take single digit at a time
        if len(digit) != 1:
            print("Enter single digit at a time!!!")
            continue
        # to check for non-numeric
        if not digit.isdigit():
            print("Enter numeric digit only!!!")
            continue
        # add digit to pin & continue next digit loop
        j += 1
        user_pin += digit
    # Pin check
    if user_pin == pin:
        print("Welcome to the system!")
        break
    else:
        if i < 3:
            print(f"Try again, Attempt: {i}/3")
        else:
            print(f"Failed Attempt: 3/3, SYSYEM LOCKED!!!")
