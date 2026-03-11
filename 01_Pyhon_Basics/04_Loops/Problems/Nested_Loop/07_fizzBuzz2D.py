# 7. THE FIZZBUZZ 2D GRID
# Print a 5x5 grid of numbers from 1 to 25.
# If a number is divisible by 3, print "Fizz".
# If a number is divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".
# Otherwise, print the number.

num = 0
for i in range(5):
    for j in range(5):
        num += 1
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
    print()
