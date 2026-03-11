# 12. THE PERFECT NUMBER DETECTIVE (Hard #23)
# Problem: Check if N is a "Perfect Number" (Sum of its proper divisors == N).
# Example: 6 is perfect because its divisors (1, 2, 3) sum to 6.
# Strategy: Find all factors (excluding the number itself) and see if their sum equals N.

N = int(input("Enter an Integer: "))
final_sum = 1  # cause 1 will always be a devisior

if N <= 1: # cause 1 is not perfect number even though (sum of it's devisiors == N
        print(f"{N} Not a perfect number :(")
else:
    for i in range(2, N // 2 + 1):  # cause devisor d for n will alway be (else then n itself) : (d <= n/2)
        if N % i == 0:
            final_sum += i
    if final_sum == N:
        print(f"{N} is Perfect number!")
    else:
        print(f"{N} Not a perfect number :(")
