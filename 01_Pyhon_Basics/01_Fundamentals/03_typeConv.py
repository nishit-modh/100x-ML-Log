# PROBLEM - input() takes string as a default 
# If we want to perform mathematical operation on user inputs
a = input("enter a")
b = input("enter b")
print(a+b) # instead of giving sum - this will give us concatinated string

# SOLUTION
# we can perform type conversion(explicit) - it has many other usecases
x = int(input("enter number for sum"))
y = int(input("enter number for sum"))
print(x+y)

# type conversion/casting - Implicit by interpreter
m = 5.2
n = 5.3
o = 10
print("type of 'o' before casting" , type(o))
o = m + n
print("type of 'o' after casting" , type(o)) # o is converted to float from int - Type casting