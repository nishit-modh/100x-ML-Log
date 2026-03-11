# 1. THE COORDINATE SKIPPER (EASY)
# Print coordinates (i, j) for a 3x3 grid (i from 1-3, j from 1-3).
# Use a nested loop, but use 'continue' to skip the coordinate if i == j.
# Expected Output: (1,2), (1,3), (2,1), (2,3), (3,1), (3,2)

n = int(input("Matrix size: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print("----- ", end="")
            continue
        print(f"({i},{j}) ",end="")
    print()