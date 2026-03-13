# 11. THE LONGEST SUBSTRING CHALLENGE
# Problem: Find the length of the longest substring that contains
# no repeating characters.
# Input: "pwwkew"
# Output: 3 (The substring is "wke")


# 1st attempt Logic: Partially Correct. Your code handles the "pww" case well, but it fails on "overlapping" substrings.
# for "dvdf" - expected output:
string = input("String: ")
string = string.lower()
longest_subs = ""
sub_string = ""
for char in string:
    if char not in sub_string:
        sub_string += char
    else:
        # Saving the record if the current streak is the longest
        if len(sub_string) > len(longest_subs):
            longest_subs = sub_string

        # PROBLEM AREA: Resetting to only the current character
        sub_string = char

print(f"Length: {len(longest_subs)}")

# ===============================================
# Correct logic - using sliding window
# ===============================================
string = input("String: ")
string = string.lower()

longest_subs = ""
sub_string = ""

for char in string:
    if char not in sub_string:
        # Keep building the current window
        sub_string += char
    else:
        # 1. Update the record before we modify the current window
        if len(sub_string) > len(longest_subs):
            longest_subs = sub_string

        # 2. THE FIX: Find where the repeat is and cut everything before it
        # If sub_string is "dv" and char is "d",
        # find "d", slice after it -> "v", then add the new "d" -> "vd"
        duplicate_index = sub_string.find(char)
        sub_string = sub_string[duplicate_index + 1 :] + char

# Final check after loop (in case the last window was the longest)
if len(sub_string) > len(longest_subs):
    longest_subs = sub_string

print(f"Longest substring: {longest_subs}")
print(f"Length: {len(longest_subs)}")
