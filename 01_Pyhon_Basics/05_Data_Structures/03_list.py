# list → Dynamic array; ordered and mutable collection

# list of numebrs
list = [10, 20, 30, 40, 50, 60]
print(list)

# list of strings
names = ["Nishit", "Dev", "Vishwa", "Nilesh"]
print(names)

# mix list
random = ["Hello", 123, list, True, 3.5, 23, False, names]
print(random)

# empty list
e_list = []
print(e_list)
print("==========")

# =======================
# indexing in list - starts with 0
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
# print(list[20]) # IndexError: list index out of range
print("==========")

# =======================
# slicing - list[start:end:step]
# sliced
print(list[2:5])
# step 2
print(list[::2])
# reverse
print(list[::-1])
print("==========")
