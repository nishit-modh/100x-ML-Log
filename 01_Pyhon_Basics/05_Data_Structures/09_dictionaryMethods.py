# =========================================================
# PYTHON DICTIONARY METHODS DEMO
# Dictionaries are MUTABLE, ORDERED (since 3.7+), and MAPPED
# They store data in KEY:VALUE pairs
# =========================================================

user = {
    "username": "coder_99",
    "email": "abc@example.com",
    "level": 5,
    "is_active": True
}

# =========================================================
# 1. RETRIEVING DATA SAFELY
# =========================================================

# get(key, default)
# → Returns the value for a key if it exists
# → If not found, returns None (instead of crashing like user["key"])
print("Email:", user.get("email"))
print("Phone:", user.get("phone", "Not Provided")) # Returns custom default

# items()
# → Returns a view object of all (key, value) tuples
print("Items:", list(user.items()))

# keys() and values()
# → Returns view objects of just keys or just values
print("Keys:", list(user.keys()))
print("Values:", list(user.values()))

print("====================================")


# =========================================================
# 2. UPDATING AND MERGING
# =========================================================

# update(iterable)
# → Merges another dictionary or iterable into the current one
# → Existing keys are overwritten; new keys are added
user.update({"level": 6, "xp": 1200})
print("After update:", user)

# setdefault(key, default)
# → If key exists, returns its value
# → If key DOES NOT exist, inserts key with the default value
# → Great for ensuring a key exists without overwriting current data
user.setdefault("theme", "Dark") 
user.setdefault("level", 10) # 'level' already exists as 6, so it stays 6
print("After setdefault:", user)

print("====================================")


# =========================================================
# 3. DELETING ELEMENTS
# =========================================================

# pop(key, default)
# → Removes the key and returns its value
# → If key is missing, returns the default (prevents KeyError)
level = user.pop("level")
print("Popped Level:", level)

# popitem()
# → Removes and returns the LAST inserted key-value pair as a tuple
last_item = user.popitem()
print("Popped Last Item:", last_item)
print("Dictionary now:", user)

# clear()
# → Removes everything from the dictionary
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print("After clear:", temp_dict)

print("====================================")


# =========================================================
# 4. CREATING DICTIONARIES FROM SCRATCH
# =========================================================

# fromkeys(iterable, value)
# → Creates a new dictionary with keys from a list/tuple
# → All keys are initialized with the same value
new_users = ["Alice", "Bob", "Charlie"]
user_status = dict.fromkeys(new_users, "Offline")
print("User Status Map:", user_status)

print("====================================")


# =========================================================
# 5. DICTIONARY COMPREHENSION (The "Pro" Trick)
# =========================================================

# Create a dictionary of squares for even numbers
# {key: value for item in iterable if condition}
nums = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in nums if x % 2 == 0}
print("Even Squares:", squares)

print("====================================")