# 5. LIST ROTATION
# Problem: Shift all elements of a list to the right by 'k' positions.
# Elements shifted off the end should reappear at the beginning.
# Example: nums = [1, 2, 3, 4, 5], k = 2 -> Output: [4, 5, 1, 2, 3]

k = int(input("Elements to shift right by: "))
nums = [1, 2, 3, 4, 5]

while k > 0:
    last_ele = nums.pop()
    nums.insert(0, last_ele)
    k -= 1
print(nums)

#=======================
# more emory efficient
#=======================
nums = [1, 2, 3, 4, 5]
k = k % len(nums) # Handles cases where k > length

# Split the list into two parts and join them
# nums[-k:] gives the last k elements
# nums[:-k] gives everything EXCEPT the last k
nums = nums[-k:] + nums[:-k]

print(nums)