"""
1. The Balanced Threshold
Take three integer inputs: a, b, and c.
Calculate a value result that is the sum of a and b multiplied by c.
Update result by finding its remainder when divided by 2.
Print True if result is 0 AND the original a is greater than b.
"""

a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
result = not (((a + b) * c) % 2)
print(result and a > b)
