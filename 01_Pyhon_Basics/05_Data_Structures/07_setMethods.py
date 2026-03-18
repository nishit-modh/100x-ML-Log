# =========================================================
# PYTHON SET METHODS DEMO
# Sets are MUTABLE collections of UNIQUE elements
# Sets are UNORDERED (no indexing) and only store IMMUTABLES
# =========================================================

my_set = {10, 20, 30}
print("Initial Set:", my_set)

# =========================================================
# 1. ADDING ELEMENTS
# =========================================================

# add(x)
# → Adds a single element to the set
# → If the element already exists, nothing happens (Uniqueness)
my_set.add(40)
my_set.add(10) # Duplicate, will be ignored
print("After add:", my_set)

# update(iterable)
# → Adds multiple elements from a list, tuple, or string
# → Flattens the input (adds each item individually)
my_set.update([50, 60, 70])
print("After update:", my_set)

print("====================================")


# =========================================================
# 2. REMOVING ELEMENTS
# =========================================================

# remove(x)
# → Removes the specified element
# → !!! Raises a KeyError if the element does not exist
my_set.remove(70)
print("After remove:", my_set)

# discard(x)
# → Removes the specified element
# → Does NOT raise an error if the element is missing (Safer)
my_set.discard(999) 
print("After discard (non-existent element):", my_set)

# pop()
# → Removes and returns a RANDOM element (since sets are unordered)
# → Raises KeyError if the set is empty
removed_val = my_set.pop()
print("After pop:", my_set)
print("Removed Value:", removed_val)

# clear()
# → Removes all elements, leaving an empty set: set()
temp_set = {1, 2, 3}
temp_set.clear()
print("After clear:", temp_set)

print("====================================")


# =========================================================
# 3. MATHEMATICAL SET OPERATIONS
# =========================================================

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# union() or |
# → Returns all elements from both sets
print("Union:", set_a.union(set_b))

# intersection() or &
# → Returns only elements present in BOTH sets
print("Intersection:", set_a & set_b)

# difference() or -
# → Returns elements in set_a that are NOT in set_b
print("Difference (a-b):", set_a - set_b)

# symmetric_difference() or ^
# → Returns elements in either set, but NOT in both
print("Symmetric Difference:", set_a ^ set_b)

print("====================================")


# =========================================================
# 4. SET RELATIONSHIPS (BOOLEANS)
# =========================================================

small_set = {1, 2}
big_set = {1, 2, 3, 4}

# issubset()
# → Returns True if all elements of 'small_set' are in 'big_set'
print("Is subset:", small_set.issubset(big_set))

# issuperset()
# → Returns True if 'big_set' contains everything in 'small_set'
print("Is superset:", big_set.issuperset(small_set))

# isdisjoint()
# → Returns True if two sets have ZERO common elements
other_set = {100, 200}
print("Is disjoint:", set_a.isdisjoint(other_set))

print("====================================")


# =========================================================
# 5. IMMUTABILITY NOTE (The "Unhashable" Rule)
# =========================================================

# You can store a Tuple in a set (Tuple is immutable)
my_set.add((1, 2, 3)) 

# You CANNOT store a List in a set (List is mutable)
# try:
#     my_set.add([1, 2]) # This would cause a TypeError
# except TypeError:
#     print("Error: Cannot store a list inside a set!")

print("Final Set with Tuple:", my_set)