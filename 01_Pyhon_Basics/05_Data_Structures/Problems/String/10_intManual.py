# 10. THE MANUAL INTEGER CONVERTER
# Problem: Take a string representing a number and convert it to 
# an actual integer without using the int() function.
# Input: "432"
# Output: 432 (as an integer type)

s = input("Number: ")
num = 0

for char in s:
    # 1. Convert character to digit
    digit = ord(char) - 48
    
    # 2. Shift the existing number left (multiply by 10) and add the new digit
    # Example "43":
    # Iteration 1: (0 * 10) + 4 = 4
    # Iteration 2: (4 * 10) + 3 = 43
    num = (num * 10) + digit

print(f"Value: {num}, Type: {type(num)}")
