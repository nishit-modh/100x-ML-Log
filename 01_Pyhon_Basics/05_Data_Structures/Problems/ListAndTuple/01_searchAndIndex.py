# 1. ELEMENT SEARCH & INDEXING
# Problem: Check if 'target' exists in 'nums'. If yes, return its index.
# If no, return -1. (Do not use .index())
# Example: nums = [10, 20, 30, 40], target = 30 -> Output: 2

nums = [11, 21, 31, 41, 51, 61, 71]
target = int(input("Search in  Nums: "))

if target not in nums:
    print("-1")
else:
    index = 0
    for num in nums:
        if num == target:
            print(index)
            break
        index += 1
