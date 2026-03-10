# 10. THE CENTERED PYRAMID (Hard #25)
# Problem: Given N, print a centered pyramid of stars.
# Input: 4
# Output:
#    *
#   ***
#  *****
# *******
# Strategy: You need to manage three things per row: Spaces, Stars, and New Lines.

# Shortcut - This first came to mind
N = int(input("Enter height of pyramid: "))
for i in range(1, N + 1):
    print(f"{' '*(N-i)}{"*"*(2*i-1)}")

# Intended in Problem - using for loop
for i in range(1, N+1): # i  =  1 to N
    for j in range(N-i): # to leave n-i spaces in start
        print(" ", end="")
    for k in range(2*i-1): # print exact number of * -> 2*i-1
        print("*", end="")
    print()# line break