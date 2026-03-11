# 4. THE FIRST DIVISOR FINDER
# Take a list of numbers: [21, 35, 9, 56].
# For each number, use a nested loop to find its first divisor (other than 1).
# Once the first divisor is found, use 'break' to stop the inner loop and move to the next number.

num_list = [21, 35, 13, 9, 56]
devisior_list = num_list
for i in devisior_list:
    # d devisior of n then ---> d <= n/2 
    for j in range(2, i//2 + 1):
        if i % j == 0:
            print(f"First devisior for {i} is {j}")
            break
    # for-else block (Python specific) - executes only if the loop completes all iterations without encountering a break statement
    else:
        print(f"{i} is a Prime Number")