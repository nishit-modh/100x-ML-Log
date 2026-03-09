# Take three sides of a triangle ($a, b, c$). Check if the sum of any two sides is greater than the third side (The Triangle Inequality Theorem).
a = int(input("Enter length of side 1: "))
b = int(input("Enter length of side 2: "))
c = int(input("Enter length of side 3: "))

# performing logical ops without using logical ops - true == 1 & false == 0
is_true = (a + b > c) + (b + c > a) + (a + c > b)

print("Triangle Inequality Theorem is: ", is_true == 3)
