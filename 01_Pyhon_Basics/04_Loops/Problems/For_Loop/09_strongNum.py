# 9. THE STRONG NUMBER CHALLENGE (Hard #24)
# Problem: Check if a number is "Strong" (Sum of factorial of digits == Number).
# Example: 145 is strong because 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Strategy: Loop through the digits, calculate factorial for each, and sum them up.

num = str(input("Enter number to check for STRONG num: "))
factorial_sum = 0

for i in num:
    i = int(i)
    fact = 1
    # to find factorial
    for j in range(1,i + 1):
            fact *= j
    factorial_sum += fact

print(factorial_sum)
if factorial_sum == int(num):
    print("This is a STRONG Number!!!")
else:
    print("Go away weak :(")