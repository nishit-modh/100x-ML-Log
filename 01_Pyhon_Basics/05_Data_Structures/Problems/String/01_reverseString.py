# 1. THE REVERSE BUILDER
# Problem: Reverse a given string without using the [::-1] shortcut.
# Input: "Gemini"
# Output: "inimeG"

s = input("String to Reverse: ")

# SHORTCUT - using slice : step = -1
# print(f"Reversed string: {s[::-1]}")

reversed_s = ""
# Start at len-1, stop before -1 (which is 0), step by -1
for i in range(len(s) - 1, -1, -1):
    reversed_s += s[i]
print(f"Reversed string: {reversed_s}")
