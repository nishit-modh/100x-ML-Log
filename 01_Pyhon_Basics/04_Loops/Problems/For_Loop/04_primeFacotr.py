# 3. THE PRIME & FACTORS DETECTIVE
# Take a number N.
# Find and print all its Factors.
# Logic Gate: If the only factors are 1 and itself, print "It is a Prime Number."
# Otherwise, print "It is a Composite Number."

num = int(input("Enter a number: "))
range_end = int(num**0.5)  # to ckeck till the sqrt
prime = True

if num < 2:
    print(f"{num} is Neither Prime nor Composite")
else:
    # Prime check - logic
    for i in range(2, range_end + 1):  # +1 to include sqrt in range
        if num % i == 0:
            prime = False
            break
    # Print prime OR factors - logic
    if prime == True:
        print(f"{num} is a Prime number.")
    else:
        print(f"Here is the list of all Factors of {num}")
        for i in range(1, (num // 2) + 1):  # Floor + 1 -> to include the output of floor devision
            if num % i == 0:
                print(f"{i}")
        print(num)  # number itself is a factor
