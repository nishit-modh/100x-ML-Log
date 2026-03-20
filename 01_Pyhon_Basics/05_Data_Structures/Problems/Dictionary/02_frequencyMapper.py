# 2. FREQUENCY MAPPER (CLEANER)
# Problem: Given a sentence, return a dictionary of word counts.
# Example: s = "apple ban apple cherry ban apple" 
# Output: {"apple": 3, "ban": 2, "cherry": 1}

# =====================================
# 1st attempt - almost perfect
# =====================================
s = "apple ban apple cherry ban apple" 
s_words = s.split()
word_count = {}

for word in s_words:
    word_count.update({word : word_count.get(word, 0) + 1 })
print(word_count)

# =====================================
# same code but without heavy - update()
# =====================================
# 2. WORD FREQUENCY MAPPER
# Goal: Count occurrences of each word in a string using .get()

s = "apple ban apple cherry ban apple" 

# STEP 1: Convert the string into a list of words
s_words = s.split()
word_count = {}

for word in s_words:
    # STEP 2: The .get() Logic
    # .get(word, 0) checks if the word exists. 
    # If YES: it returns the current count.
    # If NO: it returns 0 (the default).
    # We add 1 to whatever result we get.
    
    word_count[word] = word_count.get(word, 0) + 1
    
    # WHY NOT .update()? 
    # .update() is best for merging multiple keys at once.
    # Direct assignment [word] = ... is faster for single keys.

print(word_count) # Output: {'apple': 3, 'ban': 2, 'cherry': 1}