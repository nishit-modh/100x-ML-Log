#Take two variables, $a=5$ and $b=10$. Swap their values using only arithmetic operators (+, -), without creating a third "temporary" variable.
a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
a = a - b 
b = a + b
a = b - a
print(a,b)