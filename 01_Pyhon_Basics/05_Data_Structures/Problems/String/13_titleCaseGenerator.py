# 13. THE MANUAL TITLE CASE GENERATOR
# Problem: Capitalize the first letter of every word without built-in case methods.
# Input: "i am learning python"
# Output: "I Am Learning Python"


#===============================
# solved in 1st try - Yayyy!!!🫡🫡🫡
#===============================
default_string = input("Title: ")
default_string = default_string.split()
for i in range(len(default_string)):
    title_word = "" 
    for j in range(len(default_string[i])):
        if j == 0:
            title_word = default_string[i][j].upper()
        else:
            title_word += default_string[i][j].lower()
    default_string[i] = title_word

default_string = " ".join(default_string)
print(f"Title: {default_string}")



#===============================
# Reasoning - documentation / notes
#===============================
# 13. THE MANUAL TITLE CASE GENERATOR
# Goal: Manually capitalize every word's first letter and lowercase the rest.

default_string = input("Title: ")

# STEP 1: Split the sentence into a list of individual words.
# We do this because strings are 'immutable' (cannot be changed in place),
# but lists are 'mutable' (we can swap items out).
default_string = default_string.split()

# STEP 2: Iterate through the list using INDICES (i).
# We use range(len()) so we can overwrite the list at specific positions.
for i in range(len(default_string)):
    title_word = "" 
    
    # STEP 3: Iterate through each character (j) of the current word.
    for j in range(len(default_string[i])):
        if j == 0:
            # First letter: Convert to Uppercase
            title_word = default_string[i][j].upper()
        else:
            # All other letters: Ensure they are Lowercase
            # (This handles cases like "pYTHon" -> "Python")
            title_word += default_string[i][j].lower()
    
    # STEP 4: Update the original list at index 'i' with our newly built word.
    default_string[i] = title_word

# STEP 5: Join the list items back into a single string separated by spaces.
default_string = " ".join(default_string)

print(f"Title: {default_string}")