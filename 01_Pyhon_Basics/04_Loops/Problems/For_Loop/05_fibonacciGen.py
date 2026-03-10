# 4. THE FIBONACCI SEQUENCE GENERATOR
# Take N from the user.
# Print the first N numbers of the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
# Every new number is the sum of the previous two.
# You'll need to update your variables inside the loop.

N = int(input("Enter lenght of Fibonacci Sequence: "))
a = 0
b = 1

if N <= 0:
    print("Enter positive integer")
else:
    for i in range(N):
        print(a, end=" ")  # end=", " to skip autonext line form print()
        a, b = b, a + b  # can also write as => x = a + b : a = b : b = x
