# 5. THE SELECTIVE COORDINATE MAP
# Write nested loops to print coordinates (i, j) for a 4x4 grid.
# Requirement: Use 'continue' to skip any coordinate where i equals j.
# Requirement: Use 'break' to stop the inner loop if the sum of i + j is greater than 5.

# for 4X4 take N = 4
N = int(input("Custom Matrix Size: "))
for i in range(1,N+1):
    for j in range(1,N+1):
        if i + j > 5:
            break
        if i == j:
            print("----- ", end="")
            continue
        print(f"({i}, {j})", end=" ")
    print()