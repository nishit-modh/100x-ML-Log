# 2. THE REVERSE ENGINE
# Problem: Reverse the list 'nums' in-place WITHOUT using [::-1] or .reverse().
# Example: nums = [1, 2, 3, 4] -> Output: [4, 3, 2, 1]


#============================
# 1st attempt - not efficient for large lists - double memory due to copy being created
#============================
nums = [0, 5, 15, 25, 35, 45]
rev_nums = []
while len(nums) > 0:
    x = nums.pop()
    rev_nums.append(x)
print("Using array copy method - rev_nums: ",rev_nums)

#============================
# Two pointer approach
#============================
nums = [0, 5, 15, 25, 35, 45]

left = 0
right = len(nums) - 1

while left < right:
    # The Python Swap: a, b = b, a
    nums[left], nums[right] = nums[right], nums[left]
    
    # Move the pointers toward the middle
    left += 1
    right -= 1

print("Using two pointer method - without copy: ",nums)