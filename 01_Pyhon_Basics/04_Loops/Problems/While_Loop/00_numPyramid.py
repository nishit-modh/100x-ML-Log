# 5. THE NESTED NUMBER PYRAMID - From for loop
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
    print("Enter positive number!")
else:
    i = 1
    while i <= n:
        print(i * str(i))
        i += 1






