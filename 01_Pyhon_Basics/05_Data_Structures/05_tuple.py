# =========================================================
# PYTHON TUPLES DEMO
# Tuple → Fixed ordered collection of elements
# Tuples are IMMUTABLE → elements cannot be modified after creation
# Values can be accessed but NOT changed
# =========================================================

nums = (1, 2, 3, 4, 1, 2, 3, 4, 1, 2)

print("Tuple:", nums)

# Accessing elements using index
print("First element:", nums[0])

# Trying to modify will cause an error
# nums[1] = 20  # TypeError (tuples are immutable)

print("====================================")


# =========================================================
# 1. COUNTING OCCURRENCES
# =========================================================

# count(x)
# → Returns the number of times an element appears in the tuple
print("Count of 2:", nums.count(2))
print("Count of 1:", nums.count(1))

print("====================================")


# =========================================================
# 2. FINDING INDEX OF ELEMENT
# =========================================================

# index(x)
# → Returns the index of the FIRST occurrence of the element
print("Index of 3:", nums.index(3))

print("====================================")


# =========================================================
# 3. NEGATIVE INDEXING
# =========================================================

# Negative indexing accesses elements from the end
days = ("sun", "mon", "tue", "thurs", "fri", "sat")

print("Last day:", days[-1])
print("Second last day:", days[-2])

print("====================================")


# =========================================================
# 4. SLICING TUPLES
# =========================================================

# Slicing works similar to lists
# syntax → tuple[start:end]

print("First 4 elements:", nums[0:4])
print("Middle elements:", nums[2:6])

print("====================================")


# =========================================================
# 5. TUPLE UNPACKING
# =========================================================

# Assign tuple elements to variables directly
point = (10, 20)

x, y = point

print("x:", x)
print("y:", y)

print("====================================")


# =========================================================
# 6. SINGLE ELEMENT TUPLE
# =========================================================

# A comma is required to create a single-element tuple
single = (5,)
print("Single element tuple:", single)
print("Type:", type(single))