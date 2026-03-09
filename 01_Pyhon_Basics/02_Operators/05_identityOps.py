# identity operator
# "is" "is not"
# checks if comapred elements points to same memory location

# is
a = 10
b = 10
z = 20
print("(for 10)same momery location: ", a is b)
print(f"(for 10 and 20)Same memory location: ", a is z)
"""
python allocates this to the same location due to "Integer Interning".
The range of "Integer Interning" is -5 to 256.
"""

# is - "peephole optimization"
x = 100000
y = 100000
print("(for 100000)same momery location: ",x is y)
"""
When you run a script (or a block of code), Python looks at the whole thing before executing it. If it sees two identical large constants (like 1000) in the same code block, it says: "Hey, I’ll just create one '1000' object and point both labels to it to save memory."
"""

c = 11
d = 10+1
print("(for 11 & 10+1)same momery location: ",c is d)
"""
10+1 is a "constant expression" (it's made of fixed numbers), the Python compiler calculates it as 11 before the code even runs. It sees c = 11 and d = 11, so it points them to the same memory spot.
"""

# Type 1000 for both prompts
inp_a = int(input("Enter 1000: "))
inp_b  = int(input("Enter 1000: "))

print("Identical integers: ",inp_a == inp_b) # True (The values are the same)
print("Same memory location",inp_a is inp_b) # False (They are different objects in memory)
"""
Python doesn't know what you will type until the program is actually running, it has to create a brand-new object for each of  your input.
This way memory loaction defers.
But this only works if inputs are outside the range of "Integer Interning" which is -5 to 256.
"""

# is not
name = "Nishit"
age = 20
print(f"(is not)for {name} and {age}", name is not age)