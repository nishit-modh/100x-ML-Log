# 4. SECOND LARGEST FINDER
# Problem: Find the second largest element in a list. 
# Note: The list might contain duplicates.
# Example: nums = [10, 20, 20, 8, 15] -> Output: 15

nums = [10, 20, 20, 8, 15]
largest_2 = 0
largest = 0

for num in nums:
    if num > largest:
        largest_2 = largest
        largest = num
    elif num > largest_2 and num != largest:
        largest_2 = num
print(largest_2)