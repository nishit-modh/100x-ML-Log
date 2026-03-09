"""Goal: Take a number x. Print True if it is not in the range 10-20.
Constraint: Use not combined with a chained comparison like 10 < x < 20."""

num = int(input("Enter number between 10 to 20: "))
print("Number is valid: ", not 10 < num < 20)
