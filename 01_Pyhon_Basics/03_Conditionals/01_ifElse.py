# if elif else

# if else
a = int(input("Enter to check even-odd: "))
if a % 2 == 0:
    print("a is even: a =", a)
else:
    print("a is odd: a =", a)

# if elif else
x = int(input("Enter to find abolute value: "))
if x > 0:
    print(f"Absolue for {x} is {x}")
elif x < 0:
    print(f"Absolute for {x} is {-x}")
else:
    print(f"Given value is: {x}")
