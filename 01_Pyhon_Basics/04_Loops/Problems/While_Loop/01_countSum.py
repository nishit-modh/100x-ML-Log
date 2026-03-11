# 1. THE COUNTDOWN AND SUM
# Take an integer N. Print all numbers from N down to 1 in a single line,
# then print the total sum of those numbers.

N = int(input("Enter number N: "))
if N < 1:
    print("Enter a positive Integer!")
else:
    origanl_N = N
    total_sum = 0
    while N >= 1:
        print(f"{N}", end=" ")
        total_sum += N
        N -= 1
    print()
    print(f"Total sum of 1 to {origanl_N} is {total_sum}.")
