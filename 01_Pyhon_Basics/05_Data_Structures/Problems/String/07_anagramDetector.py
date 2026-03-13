# 7. THE ANAGRAM DETECTOR
# Problem: Check if two strings are anagrams of each other (contain the 
# same characters in different orders).
# Input: "silent", "listen"
# Output: True

# a = "listen"
# b = "silent"

# The "Smart" Way
a = input("Str 1: ").lower()
b = input("Str 2: ").lower()

if len(a) != len(b):
    print("Not an anagram")
else:
    if sorted(a) == sorted(b):
        print("Is an anagram")
    else:
        print("Not an anagram")

# using count()
a = a.lower()
b = b.lower()
is_anagram = len(a) == len(b) # Start with length check

checked = ""
if is_anagram:
    for char in a:
        if char not in checked:
            if a.count(char) != b.count(char):
                is_anagram = False
                break # Exit as soon as a mismatch is found
            checked += char
if is_anagram:
    print(f"{a} and {b} are anagram.")
else:
    print(f"{a} and {b} are not anagram.")

