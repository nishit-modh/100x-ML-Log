# 10. MANUAL SORT (BUBBLE SORT)
# Problem: Sort a list in ascending order without using .sort() or sorted().
# Example: nums = [64, 34, 25, 12, 22] -> Output: [12, 22, 25, 34, 64]

#========================
# 1st attempt - works but more like neighbor swap - O(N**2) every time
#========================
nums = [64, 34, 25, 12, 22]
i = 0
while i in range(len(nums)):
    j = 0
    while j in range(len(nums)):
        if j < len(nums) - 1:
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        j += 1
    i += 1
print(nums)

#=========================
# Bubble sort with early exit - the real bubble sort - 
# O(N**2) in average and worst case
# O(N) in best case - already sorted
#=========================
nums = [64, 34, 25, 12, 22]
n = len(nums)

for i in range(n):
    swapped = False
    
    # Range is n - i - 1 because the last 'i' elements are already sorted
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True
            
    # If no two elements were swapped by inner loop, then break
    if not swapped:
        break

print(f"Sorted list: {nums}")