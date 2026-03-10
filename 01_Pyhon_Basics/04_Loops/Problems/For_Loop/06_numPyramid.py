# 5. THE NESTED NUMBER PYRAMID
# Create a triangle pattern based on N.
# Example Input: 4
# Output:
# 1
# 22
# 333
# 4444
# Challenge: Use a nested for loop (one loop inside another).

n = int(input("Enter a number: "))
if n <= 0:
    print("Enter positive number")
else:
    for i in range(1, n +1):
        for j in range(i):
            print(i, end=" ")
        print()

# Using While loop - more efficient
"""
n = int(input("Enter a number: "))
if n <= 0:
    print("Enter positive number")
else:
    i = 1
    while i <= n:
        print(f"{str(i)*i}")
        i += 1
"""
