# 6. FREQUENCY MAPPER
# Problem: Count the occurrences of each element and return as a Dictionary.
# Example: nums = [1, 2, 2, 3, 1, 1] -> Output: {1: 3, 2: 2, 3: 1}

#================================
# using count - LEss efficient = O(N**2)
#================================
nums = [1, 2, 2, 3, 1, 1]
counted = {}
for num in nums:
    if num not in counted:
        counted[num] = nums.count(num)
print(counted)


#================================
# efficient way - by incrimenting the count - O(N)
#================================
nums = [1, 2, 2, 3, 1, 1]
counted = {}

for num in nums:
    if num in counted:
        counted[num] += 1  # Already saw it? Just add 1 to the tally
    else:
        counted[num] = 1   # First time seeing it? Set it to 1
        
print(counted)