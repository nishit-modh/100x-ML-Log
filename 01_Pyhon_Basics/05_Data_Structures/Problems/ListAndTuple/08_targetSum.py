# 8. THE TARGET SUM PAIRS
# Problem: Find all unique pairs in 'nums' that add up to a 'target' sum.
# Example: nums = [1, 2, 3, 4, 5], target = 6 -> Output: [(1, 5), (2, 4)]


#==================================
# O(N**2)
#==================================
nums = [1, 2, 3, 4, 5]
# target = int(input("Target sum: "))
target = 6
paired_index = []
pairs = []
for i in range(len(nums)):
    if i not in paired_index:
        pair = target - nums[i]
        if pair in nums and nums.index(pair) != i:
            pairs.append((nums[i], pair))
            paired_index.append(nums.index(pair))
        paired_index.append(i)
print(pairs)


#=====================================
# Efficient - Sort and Two pointer solution - O(N)
#=====================================
nums = [1, 2, 3, 4, 5]
target = 6

# Step 1: Ensure the list is sorted (The logic depends on order)
nums.sort() 

pairs = []
left = 0
right = len(nums) - 1

while left < right:
    current_sum = nums[left] + nums[right]
    
    if current_sum == target:
        pairs.append((nums[left], nums[right]))
        left += 1   # Move both pointers inward
        right -= 1
    elif current_sum < target:
        # We need a bigger sum, move the left pointer forward
        left += 1
    else:
        # We need a smaller sum, move the right pointer backward
        right -= 1

print(pairs) # [(1, 5), (2, 4)]