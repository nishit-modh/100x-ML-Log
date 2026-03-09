# Take two integers. Print True only if one is even and the other is odd. (Hint: Use % and !=).
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
print(f"Are the numbers in even-odd pair: ({num_1%2 != num_2%2})")
