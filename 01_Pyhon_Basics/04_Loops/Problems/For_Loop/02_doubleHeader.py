"""
1. The Digits "Double-Header"
Take a large integer $N$ from the user.:
- Calculate the Sum of all digits.
- Count how many Even digits and how many Odd digits it contains.
- Example: Input 1234 => Sum: 10, Even: 2, Odd: 2.
"""

num = str(input("Enter a number: "))
even = 0
odd = 0
total_sum = 0
for i in num:
    i = int(i)
    total_sum += i
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Sum: {total_sum}, Even: {even}, Odd: {odd}")
