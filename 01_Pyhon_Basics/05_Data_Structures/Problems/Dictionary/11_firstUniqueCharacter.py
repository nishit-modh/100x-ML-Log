# 11. FIRST UNIQUE CHARACTER👍
# Problem: Find the index of the first character in a string that does not repeat.
# Example: s = "alphabet" -> Output: 1 (since 'l' is the first non-repeating char)

# ---------------------------------------------------------
# VERSION 2: THE "BLACKLIST" STRATEGY (Best Performance)
# Logic: Use a Dict to store the index OR a "Trash" marker.
# ---------------------------------------------------------
s = "aaabcaabsks"
char_index = {}

# Pass 1: Categorize every character
for i, char in enumerate(s):
    if char not in char_index:
        # If new: store its original index
        char_index[char] = i
    else:
        # If seen again: "Blacklist" it with -1 (Not Unique)
        char_index[char] = -1

# Pass 2: Find the first valid index
# Since Python 3.7+ dicts preserve order, the first key 
# with a value >= 0 is the true FIRST unique character.
for char in char_index:
    if char_index[char] >= 0:
        print(f"Result (Blacklist Method): {char_index[char]}")
        break

# ---------------------------------------------------------
# VERSION 3: THE "TRUE FREQUENCY" METHOD (Most Readable)
# Logic: Count everything first, then check the string again.
# ---------------------------------------------------------
counts = {}

# Step 1: Build a pure frequency map {char: count}
for char in s:
    counts[char] = counts.get(char, 0) + 1

# Step 2: Loop through string to find the first char with count 1
result = -1
for i, char in enumerate(s):
    if counts[char] == 1:
        result = i
        break

print(f"Result (Frequency Method): {result}")