"""
# this is just trash - not good problem
3. The Bitwise-Style Swap & Check
Take two variables x and y from user input.
- Add y to x using an assignment operator.
- Subtract the new x from y using an assignment operator.
Multiply x by -1.
Print True if the final x is identical in value to the original y OR if the final y is positive.
"""

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
origin_y = y
x += y
y -= x
x *= -1
print(x == origin_y or y > 0)
