# 2. THE MULTIPLICATION MATRIX
# Print a multiplication table for numbers 1 through 5.
# Use nested loops so that the output looks like a square matrix.
# Expected Output:
# 1  2  3  4  5
# 2  4  6  8  10
# ... up to 5x5

for i in range(1,6):
    for j in range(1,6):
        print(f"{i*j} ", end="")
    print()