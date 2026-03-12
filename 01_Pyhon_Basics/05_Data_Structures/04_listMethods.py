import copy

# =========================================================
# PYTHON LIST METHODS DEMO
# Lists are MUTABLE → elements inside a list can be modified
# =========================================================

nums = [10, 20]
print("Initial List:", nums)

# =========================================================
# 1. ADDING ELEMENTS TO A LIST
# =========================================================

# append(x)
# → Adds ONE element at the end of the list
# → Only one argument can be passed at a time
nums.append(30)
print("After append:", nums)

# extend(iterable)
# → Adds multiple elements from another iterable
# → Elements are added individually to the list
extra_nums = [40, 50, 60]
nums.extend(extra_nums)
print("After extend:", nums)

# extend() can also take strings
# → Each character is added separately
char_list = []
char_list.extend("Human")
print("Characters:", char_list)

# insert(index, value)
# → Inserts a value at a specific index position
nums.insert(2, 25)
print("After insert:", nums)

print("====================================")


# =========================================================
# 2. REMOVING ELEMENTS FROM A LIST
# =========================================================

# remove(x)
# → Removes the FIRST occurrence of the specified value
nums.remove(25)
print("After remove:", nums)

# pop(index)
# → Removes an element at a specific index
# → If index is not provided, it removes the LAST element
# → The removed value is returned and can be stored
removed = nums.pop()
print("After pop:", nums)
print("Removed element:", removed)

print("====================================")


# =========================================================
# 3. SORTING LISTS
# =========================================================

marks = [57, 74, 82, 1, 91, 378, 12, 46, 63, 46]

# index(x)
# → Returns the index of the FIRST occurrence of the value
print("Index of 1:", marks.index(1))

# sort()
# → Sorts the list in ascending order
marks.sort()
print("Sorted ascending:", marks)

# sort(reverse=True)
# → Sorts the list in descending order
marks.sort(reverse=True)
print("Sorted descending:", marks)

# Sorting also works for strings
letters = ["a", "Z", "d", "A", "c", "F", "z"]

letters.sort()
print("Letters sorted:", letters)

letters.sort(reverse=True)
print("Letters reverse sorted:", letters)

print("====================================")


# =========================================================
# 4. COUNTING OCCURRENCES
# =========================================================

nums = [1, 1, 1, 2, 3, 4, 4, 5, 5, 5, 3, 4, 1, 2, 3, 2, 1]

# count(x)
# → Returns the number of times an element appears in the list
print("Count of 1:", nums.count(1))
print("Count of 2:", nums.count(2))

# If the element does not exist → count returns 0
print("Count of 0:", nums.count(0))

print("====================================")


# =========================================================
# 5. REFERENCE COPY (NOT A REAL COPY)
# =========================================================

a = [10, 20, 30]

# Both variables point to the SAME memory reference
# Any modification using one variable affects the other
b = a
b.append(40)

print("a:", a)
print("b:", b)

print("====================================")


# =========================================================
# 6. SHALLOW COPY USING copy()
# =========================================================

# copy()
# → Creates a new outer list
# → Inner objects are still shared if they exist

c = a.copy()
c.append(50)

print("a:", a)
print("c:", c)

print("====================================")


# =========================================================
# 7. SHALLOW COPY WITH NESTED LISTS
# =========================================================

x = [1, 2, [3, 4]]

y = x.copy()
y[2].append(5)

# copy() only creates a new outer list
# Inner lists are still shared (shallow copy behavior)
# Therefore changes to the inner list affect both lists
print("x:", x)
print("y:", y)

print("====================================")


# =========================================================
# 8. TRUE DEEP COPY
# =========================================================

# deepcopy()
# → Creates a completely independent copy
# → Both outer list and inner elements are duplicated

y = copy.deepcopy(x)
y[2].append(6)

# Now changes in y will NOT affect x
print("x:", x)
print("y:", y)

print("====================================")
