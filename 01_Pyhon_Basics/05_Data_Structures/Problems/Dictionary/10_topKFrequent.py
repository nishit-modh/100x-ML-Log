# 10. TOP 'K' FREQUENT👍
# Problem: Return the k most frequent elements in a list.
# Example: nums = [1, 1, 1, 2, 2, 3], k = 2 -> Output: [1, 2]


# ====================================
# self made logic - google help for syntax
# ====================================
nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
counted = dict()
k = int(input("K: "))

# LOGIC:
# 1. Loop through 'nums' one by one.
# 2. Check if we've already counted this number.
# 3. If NOT: call nums.count(num).
#    !!! THIS IS THE PROBLEM: .count() loops through the WHOLE list again.
#    If the list has 1,000 items, and 500 are unique, Python does 500,000 checks.
# 4. Sort the result by the frequency (value) using a lambda.
for num in nums:
    if num not in counted:
        repeat = nums.count(num)  # Hidden loop inside a loop!
        counted[num] = repeat

# to get reverse dict as per item values
counted = dict(sorted(counted.items(), key=lambda item: item[1], reverse=True))
k_frequent_list = list(counted.keys())

print(k_frequent_list[:k])

# =====================================
# more efficient way
# =====================================
nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
counted = dict()
k = int(input("K: "))

# LOGIC:
# 1. Use .get(num, 0) + 1 to build the frequency map in a single pass.
#    No nested loops! If the list has 1,000 items, Python does 1,000 checks.
# 2. 'frequent_board' uses a sorted view of the dictionary items.
# 3. lambda item: item[1] tells sorted() to look at the VALUE (the count).
# 4. Slices the first 'k' keys from the result.
for num in nums:
    # If num exists, get count and add 1. If not, start at 0 and add 1.
    counted[num] = counted.get(num, 0) + 1

# Sorting O(N log N) is much faster than the O(N^2) counting method above.
frequent_board = dict(sorted(counted.items(), key=lambda item: item[1], reverse=True))
frequent_list = list(frequent_board.keys())

print(frequent_list[:k])
