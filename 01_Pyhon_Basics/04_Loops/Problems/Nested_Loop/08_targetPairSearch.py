# 8. THE TARGET PAIR SEARCH (Matrix Break)
# Create a 10x10 multiplication table (1-100).
# Search for the first pair of numbers (i, j) whose product is exactly 57.
# When found, print the pair and stop BOTH loops immediately.

# target = 57
target = int(input("Enetr target: "))
found = False
for i in range(1, 11):
    if found:
        break
    for j in range(1,11):
        print(f"{j} X {i} = {j*i}", end=" | ")
        if j*i == target:
            found = True
            break
    print()

# for else method
"""
for i in range(1, 11):
    for j in range(1, 11):
        if i * j == target:
            print(f"Found: {i} x {j}")
            break # Breaks inner loop
    else:
        continue # Only runs if inner loop DID NOT find the target
    break # Only runs if inner loop DID find the target (skipping the continue)
"""