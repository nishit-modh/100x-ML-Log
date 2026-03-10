# 6. THE SEARCH & DESTROY VOWEL FILTER
# Take a sentence from the user.
# Create a new string that contains only the consonants from the original sentence.
# (Removes all vowels: a, e, i, o, u).
# Print the final result and the count of how many characters were removed.

s = str(input("Enter a String: "))
vowels = "aeiouAEIOU"
removed = 0
clean_s = ""

for char in s:
    if char in vowels:
        removed += 1
    else:
        clean_s += char
print(f"Final string after removing {removed} vowels is {clean_s}")

# flawed logic - correct output
"""
s = str(input("Enter a String: "))
vowels = "aeiou"
removed = 0
for i in s:
    for j in vowels:
        if i == j:
            removed += 1
            s = s.replace(i, "")
print(f"Final string after removing {removed} vowels is {s}")
"""
