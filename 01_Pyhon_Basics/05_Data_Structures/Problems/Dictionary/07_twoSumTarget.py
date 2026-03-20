# 7. THE TWO-SUM (OPTIMAL)
# Goal: Find indices of two numbers that sum to target in ONE pass.
# Example: nums = [2, 7, 11, 15], target = 9 -> Output: [0, 1]

# ================================
# old method - without dictionary
# this won't work to get indices - cause operations on sorted array
# ================================

target = int(input("Target: "))
nums = [2, 7, 11, 3, 15, 6, 1, 28, 3, 8, 9, 17]
nums.sort()

left = 0
right = len(nums) - 1
pairs = set()

while left < right:
    if nums[left] + nums[right] < target:
        left += 1
    elif nums[left] + nums[right] > target:
        right -= 1
    else:
        pairs.add((nums[left], nums[right]))
        left += 1
        right -= 1

print(pairs)

# ================================
# using dictionary
# ================================

nums = [2, 7, 11, 3, 15, 6, 1, 28, 3, 8, 9, 17]
target = int(input("Target: "))

seen = {}
paired = dict()
for i, n in enumerate(nums):
    complement = target - nums[i]
    if complement in seen:
        paired[seen[complement]] = i
    seen[n] = i
print(paired)


# #================================
# # solution - with commented logic - same as above
# #================================
nums = [2, 7, 11, 3, 15, 6, 1, 28, 3, 8]
target = int(input("Target: "))

# This dictionary will store { Number : Index }
seen = {}

# We use enumerate to get both the index (i) and the value (n)
for i, n in enumerate(nums):
    complement = target - n

    # 1. Check if the "partner" we need has been seen already
    if complement in seen:
        # If found, return the index of the partner and current index
        print(f"Indices: [{seen[complement]}, {i}]")
        # break # break if only one pair needed

    # 2. If not found, add current number to the dictionary
    seen[n] = i

# Logic Trace:
# 1. i=0, n=2. Complement = 7. Is 7 in 'seen'? No. Add {2: 0} to 'seen'.
# 2. i=1, n=7. Complement = 2. Is 2 in 'seen'? YES! Return [seen[2], 1] -> [0, 1].
