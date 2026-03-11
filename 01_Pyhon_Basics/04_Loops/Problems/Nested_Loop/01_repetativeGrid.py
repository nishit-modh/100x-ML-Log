# 1. THE REPETITIVE GRID
# Print a 5x5 grid where each row contains numbers from 1 to 5.
# Use nested loops.
# Expected Output:
# 1 2 3 4 5
# 1 2 3 4 5 (and so on...)

# 5X5 grid if n == 5
n = int(input("Requred no of rows: "))
for i in range(n):
    for j in range(1,6):
        print(f"{j} ", end="")
    print()