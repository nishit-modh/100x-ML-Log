"""
Take a number. Print:
"FizzBuzz" if divisible by both 3 and 5.
"Fizz" if divisible by 3.
"Buzz" if divisible by 5.

Otherwise, print the number.
Challenge: Make sure "FizzBuzz" prints correctly
"""

num = int(input("Enter the number: "))
if (num % 3 == 0) and (num % 5 == 0):
    print("FizzBuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
