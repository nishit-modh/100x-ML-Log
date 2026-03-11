# 3. THE SELECTIVE TRIANGLE
# Print a number triangle up to N rows.
# Use a nested loop, but use the 'continue' keyword to skip printing the number 3 
# in every row where it would usually appear.

N = int(input("Height for triangle: "))
for i in range(1, N+1):
    for j in range(1,i+1):
        if j == 3:
            continue
        print(f"{j}", end=" ")
    print()