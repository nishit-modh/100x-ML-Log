# 11. THE NUMBER PALINDROME PYRAMID
# Use only while loops to print a centered number palindrome pyramid.
# Input: 3
# Output:
#   1
#  121
# 12321

# THe Math way
num = int(input("Pyramid Height: "))
i = 1
while i <= num:
    # for num - i spaces
    j = num - i
    while j > 0:
        print(" ", end="")
        j -= 1
    k = 1
    while k < 2 * i:
        # for k == 1 to k == i
        if k <= i:
            print(k, end="")
        # for k > i
        else:
            print(i * 2 - k, end="")
        k += 1
    # new line and incremen i for next i
    print()
    i += 1

# The shortcut
number = int(input("Pyramid Height: "))
i = 1
while i <= number:
    # skip while loop using - string manipulation
    print((number - i) * " ", end="")
    k = 1
    while k < 2 * i:
        # for k == 1 to k == i
        if k <= i:
            print(k, end="")
        # for k > i
        else:
            print(i * 2 - k, end="")
        k += 1
    # new line and incremen i for next i
    print()
    i += 1
