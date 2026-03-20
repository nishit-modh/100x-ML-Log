# 5. CATEGORY GROUPER
# Problem: Group a list of words by their starting letter into a dictionary of lists.
# Example: words = ["apple", "ant", "bat", "ball", "cat"]
# Output: {"a": ["apple", "ant"], "b": ["bat", "ball"], "c": ["cat"]}


# ================================
# 1st attempt - perfect pythonic logic - YAY
# ================================
words = ["apple", "ant", "bat", "ball", "cat"]
grouped = {}

for word in words:
    grouped[word[0]] = grouped.get(word[0], [])
    grouped[word[0]].append(word)
print(grouped)


# ================================
# USING - # defaultdict → Dictionary with automatic default values
# ================================
from collections import defaultdict

words = ["apple", "ant", "bat", "ball", "cat"]
grouped = defaultdict(list)  # Automatically creates a list for new keys

for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))