# 6. THE PRIME RANGE DISCOVERY
# Find and print all prime numbers between 2 and 50.
# Use an outer loop to iterate through the numbers and an inner loop
# to check for factors. Use 'break' to optimize the inner loop.

# for 2 to 50 --> a = 2 and b = 50
a = int(input("a: "))
b = int(input("b: "))
# for stating range from prime numbers - skipping 0 and 1
if a < 2:
    a = 2
print("Prime numbers are: ", end="")
for i in range(a, b + 1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")

# The "For-Else" Alternative:
"""
for i in range(a, b+1):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
"""