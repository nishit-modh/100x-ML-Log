# 10. THE N-DIGIT ARMSTRONG CHECKER
# Check if a number is an Armstrong number. A number is Armstrong if the 
# sum of its digits raised to the power of the number of digits equals the number.
# exa : 153: 1^{3} + 5^{3} + 3^{3} = 1 + 125 + 27 = 153 (3 digits)

N = int(input("Check Armstrong for: "))
N = abs(N) # works only on positive nums
n = N

# shortcut for finding length
# length = len(str(n))

# manual way - fonding length
length = 0
while n > 0:
    n //= 10
    length += 1


# findinng sum of power of digits
n = N
total = 0
while n > 0:
    last_digit = n % 10 
    n //= 10
    last_digit **= length
    total += last_digit

# check for armstrong
if total == N:
    print(f"{N} is An Armstrong number!!!")
else:
    print(f"{N} is not Armstrong Number!")