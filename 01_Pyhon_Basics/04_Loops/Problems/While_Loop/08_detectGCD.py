# 8. THE GCD DETECTIVE (Greatest Common Divisor)
# Take two integers A and B. Use a while loop to find the highest number 
# that divides both without a remainder.

#Using Euclid's algo
A = int(input("A: "))
B = int(input("B: "))

# Step 1: Handle negatives by making them positive
x, y = abs(A), abs(B)

# Step 2: The Euclidean Loop
# We continue until the 'remainder' (y) becomes 0
while y != 0:
    # Python Shortcut: x becomes y, y becomes the remainder
    x , y = y , x % y
print(F"GCD of {A} and {B}: {x}")


# Eucild's algo is optimum
# 1. No need for seperate number swap logic :
#   x= 12 and y = 18
#   x , y = y , x % y ==> x = y so (x = 18) && y = x % y so( y = 12 cause 12 % 18 == 12 )
#   x = 18 and y = 12 - number swaped automatically