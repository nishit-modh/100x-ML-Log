# str → Immutable sequence of characters (text data)

# string creation - using " " OR ' '
name = "Python"

# length function
print(len(name))
print("======")

# ============================================
# string indexing - starts from 0
print(name[0])
print(name[1])
print(name[5])
print("======")

#  for 50 => IndexError: string index out of range
# print(name[50])

# Negative Indixing - starts from ending
# -1 is last cahracter
print(name[-1])
print(name[-2])
print(name[-6])
print("======")

# for -16 => IndexError: string index out of range
# print(name[-16])

# ============================================
# Immutable => TypeError: 'str' object does not support item assignment
# you have to reassign name completely to change => name = "Bython" for change
# name[0] = "B"

# ============================================
# slicing name[start:end:step] - selected part of string
# str[1:3] - index : 0(X), 1, 2, 3(X), 4(X)...
print(name)
print(name[0:4])

# Slicing with steps

# step = 2 will skip every other number
print(name[0:6:2])

# step = (-1) will reverse the string
# default start --> 0
# if end = enpty --> traverses the whole string
print(name[::-1])
print("======")