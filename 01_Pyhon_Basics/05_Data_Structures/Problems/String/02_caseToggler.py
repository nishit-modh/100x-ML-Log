# 2. THE CASE TOGGLER
# Problem: Convert all uppercase characters to lowercase and vice versa. 
# Do not use .swapcase().
# Input: "PyThOn 3.10"
# Output: "pYtHoN 3.10"

s = input("String to Swapcase: ")
swaped_s = ""
for char in s:
    # for upper to lower
    if char.isupper() :
        swaped_s += char.lower()
    # for lower to upper
    elif char.islower():
        swaped_s += char.upper()
    # fro not-alphabetic character
    else:
        swaped_s += char
print(swaped_s)