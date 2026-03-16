# 7. PALINDROME LIST CHECK
# Problem: Check if a list reads the same forward and backward.
# Example: nums = [1, 2, 3, 2, 1] -> Output: True

#================================
# 1st attempt - split and compare
#================================
nums = [1, 2, 3, 2, 1]
if nums[0 : len(nums) // 2] == nums[len(nums) - 1 : (len(nums) // 2) : -1]:
    print(f"{nums} is palindrome list")
else:
    print(f"{nums} is not palindrome list")

#================================
# Two pointer method
#================================
nums = [1, 2, 3, 2, 1]
is_palindrome = True

for i in range(len(nums) // 2):
    if nums[i] != nums[-(i + 1)]:
        is_palindrome = False
        break

print(f"Is Palindrome: {is_palindrome}")

#================================
# correction in method 1 - no need to check only half
#================================
# check nums vs rev_nums
nums = [1, 2, 3, 2, 1]

if nums == nums[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")