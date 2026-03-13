# 5. THE WORD REVERSER
# Problem: Reverse the order of words in a sentence, but keep the characters 
# within the words in the correct order. Do not use .split().
# Input: "Learning is fun"
# Output: "fun is Learning"

s = input("Input string: ")
temp_s = ""
rev_s = ""
# to enter space at last for including last word
for char in s + " ":
    if char == " ":
        temp_s = temp_s + char 
        # for 1st iteration(of Space)
        # rev_s = "Learning" + "" = "Learning" 
        #for 2nd iteration(of Space) 
        # rev_s = "is" + "Learning" = "is Learning"
        rev_s = temp_s + rev_s
        #reset temp_s
        temp_s = ""
    # build new temp_s
    else:
        temp_s += char 
print(rev_s)

# Shortcut using split()
# split() - splits any white space 
"""
split() handles the words.
[::-1] reverses the list.
join() builds the final string in one go (memory efficient).
"""
result = " ".join(s.split()[::-1])
print(result)
