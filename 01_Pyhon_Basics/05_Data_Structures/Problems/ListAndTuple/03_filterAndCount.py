# 3. FILTER & COUNT
# Problem: Given a list of numbers, return a new list containing
# only the even numbers that are greater than 10.
# Example: nums = [2, 12, 5, 18, 8, 22] -> Output: [12, 18, 22]

nums = [4, 6, 7, 9, 13, 18, 22, 31, 42]
new_list = []
for num in nums:
    if num > 10 and num % 2 == 0:
        new_list.append(num)
print(new_list)

#================================
# The python one liner way
#================================
# [expression for item in list if condition]
new_list = [num for num in nums if num > 10 and num % 2 == 0]
print(new_list)