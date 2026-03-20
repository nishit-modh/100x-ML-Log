# 8. ANAGRAM GROUPER
# Problem: Group words that are anagrams of each other into sub-lists.
# Example: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagram = defaultdict(list)

for word in words:
    sorted_char = sorted(word)
    sorted_key = "".join(sorted_char)
    anagram[sorted_key].append(word)

print(anagram.values())