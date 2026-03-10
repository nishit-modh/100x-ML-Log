# 11. THE NUMBER PALINDROME PYRAMID
# Problem: Given an integer N, print a centered number palindrome pyramid.
# Example: Input: 3
# Output:
#   1
#  121
# 12321

N = int(input("Enter height of pyramid: "))
for i in range(1, N+1):# iterate till 1 to N
    for j in range(N-i): # N-1 spaces at the start
        print(" ", end="")
    for k in range(1 ,i*2): # 1 to i*2 range - for i*2-1 outputs : cause startign with 1
        if k<= i:
            print(k, end="") # print in order till k == i
        else:
            print(2*i-k, end="")# then printing 2i - k
    print()
"""
How your math works (Row 3, i=3):
Range is 1 to 5.
k=1, 2, 3 : Prints 1, 2, 3 (since k <= i).
k=4: 2(3) - 4 = 2.
k=5: 2(3) - 5 = 1.
Result: 12321. Verified!
"""