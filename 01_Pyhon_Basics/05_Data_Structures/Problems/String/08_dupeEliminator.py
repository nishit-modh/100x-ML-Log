# 8. THE DUPLICATE ELIMINATOR
# Problem: Remove all duplicate characters from a string, keeping 
# only the first occurrence.
# Input: "success"
# Output: "suce"

a = "sucess"
og = ""

for char in a:
    if char not in og:
        og += char
print(og)