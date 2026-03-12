# 4. THE CLEAN PALINDROME
# Problem: Check if a string is a palindrome, ignoring spaces and capitalization.
# Input: "Race Car"
# Output: True (Since "racecar" is the same backwards)

palindrom_check = input("Check palindrome: ")
s = palindrom_check
s = s.lower().replace(" ","")
if s == s[::-1]:
    print(f"{palindrom_check} is a paindrome string.")
else:
    print(f"{palindrom_check} is not a palindrome string!!!")

# without using [::-1] shortcut
is_palindrome = True
# iterates s starting from 0 to center element
# cause we are checking to the center from both side - start and end
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        is_palindrome = False
        break # stop immediately
if is_palindrome:
    print(f"{palindrom_check} is a paindrome string.")
else:
    print(f"{palindrom_check} is not a palindrome string!!!")