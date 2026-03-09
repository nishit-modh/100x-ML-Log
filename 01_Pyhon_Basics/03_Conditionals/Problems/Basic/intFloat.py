"""
6. Integer or Float?
Take a float input. Check if the number is actually an integer (e.g., 5.0 is an integer, 5.5 is not).
"""
num = float(input("Enter the number: "))
if (num%1) == 0:
    print("This is an Integer")
else:
    print("This is a Float")