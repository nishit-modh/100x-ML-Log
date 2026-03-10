# 2. THE CHARACTER CASE COUNTER
# Take a string S from the user.
# Count the Uppercase, Lowercase, and Spaces separately.
# Challenge: Also calculate the Percentage of the string that is Uppercase.

s = str(input("Enter a String: "))
upper_case = 0
lower_case = 0
spaces = 0
for i in s:
    if i.isupper():
        upper_case += 1
    elif i.islower():
        lower_case += 1
    elif i.isspace():
        spaces += 1
    else:
        pass
if len(s) > 0:
    print(
        f"Uppercase: {upper_case}, Lowercase: {lower_case}, Spaces: {spaces} | Uppercase Percentage: {(100*upper_case)/len(s)}"
    )
else:
    print("Hey, Enter a string!")