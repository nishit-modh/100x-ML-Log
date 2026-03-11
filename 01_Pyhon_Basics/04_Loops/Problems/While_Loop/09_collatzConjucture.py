# 9. THE COLLATZ CONJECTURE
# Take an integer N. While N != 1: If even, N = N/2; if odd, N = 3N + 1.
# Print every step and the total count of steps to reach 1.

N = int(input("Collatz conjecture for: "))
n = N
max = N
if N <= 1:
    print("Number must be Greater than 1!!!")
else:
    count = 0
    while N != 1:
        if N % 2 == 0:
        # for even numbers
            print(f"{N} (even) -> {N} / 2 = {N/2}")
            # floor devision fro inproved accuracy in larger numbers
            N //= 2
        else:
        # for odd numbers
            print(f"{N} (odd) -> (3 X {N}) + 1 = {(N*3)+1}")
            N = N * 3 + 1
            if N > max:
                max = N
        count += 1
    print(f"Collatz conjecture for {n} can be found in {count} steps")
    print(f"Maximum value reached: {max}")
