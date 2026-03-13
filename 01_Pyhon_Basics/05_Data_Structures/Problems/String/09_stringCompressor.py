# 9. THE STRING COMPRESSOR
# Problem: Compress a string by replacing consecutive repeating 
# characters with the character followed by the count.
# Input: "aaabbccccd"
# Output: "a3b2c4d1"

# The manual OR JS way - the same question I did in JS
# but JS logic wont work in python - both handles out of bound errors differently
a = input("String: ")
# a = "aaabbcccccddaaa"

if not a:
    print("")
else:
    z = ""
    count = 1
    
    # We start at 1 because we always look BACK at i-1
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            # Still the same character, just increase the tally
            count += 1
        else:
            # The character CHANGED! 
            # 1. Record the character that just finished (a[i-1])
            # 2. Record how many times we saw it (count)
            z += f"{a[i-1]}{count}"
            
            # Reset count for the NEW character we just encountered
            count = 1
            
    # CRITICAL STEP: The loop finishes when it hits the end of the string.
    # The very last group of characters never triggered the 'else' block.
    # So we manually add the last character and its count here.
    z += f"{a[-1]}{count}"

    print(z)


# The "Pythonic" Manual Way (Optimized for Speed)
a = "aaabbcccccddaaa"
parts = [] # Using a list for memory efficiency (O(N))
count = 1

for i in range(len(a)):
    # LOOK-AHEAD LOGIC:
    # We check: 
    # 1. Are we NOT at the very last character? (i + 1 < len(a))
    # 2. Is the NEXT character the same as the current one?
    if i + 1 < len(a) and a[i] == a[i+1]:
        count += 1
    else:
        # If we are at the last character of a group, OR the end of the string:
        # Record the current character and the total count accumulated
        parts.append(f"{a[i]}{count}")
        
        # Reset count for the next sequence
        count = 1

# Join all parts into one final string (The most efficient way in Python)
print("".join(parts))