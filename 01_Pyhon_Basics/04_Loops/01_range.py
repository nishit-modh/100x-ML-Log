"""
Range : generates an immutable sequence of integers - most commonly used in for loops
- range(stop), range(start, stop), or range(start, stop, step)

Argument 	                Description	                           Default Value
start	    The starting integer of the sequence (inclusive).      - 	 0
stop	    The ending integer of the sequence (exclusive).	       -  Required
step	    The difference between each number in the sequence.	   -     1
"""

print(list(range(10)))  # print range 0 to 9 - By default start from 0 and 10 is exclusive
print(list(range(1, 6)))  # print range 1 to 5 - 1 inclusive and 6 exclusive
print(list(range(5, 0, -1)))  # print range 5 to 1 - (-1) reverses the order
print(list(range(1, 21, 2)))  # print range 1 to 20 - (2) is stpe so : 1,3,5 - odd numbers