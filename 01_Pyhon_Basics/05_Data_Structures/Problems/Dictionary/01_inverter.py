# 1. THE INVERTER
# Problem: Swap keys and values in a dictionary.
# (Assume all values are unique and immutable).
# Example: d = {"a": 1, "b": 2, "c": 3} -> Output: {1: "a", 2: "b", 3: "c"}

#=======================
# 1st attempt
#=======================
d = {"a": 1, "b": 2, "c": 3, "d": 1}
inverted_d = {}
for key, value in d.items():
    inverted_d.setdefault(value, key)
print(inverted_d)

# ================================
# pythonic one-liner
# ================================
inverted_d = {v: k for k, v in d.items()}
print(inverted_d)

# ================================
# To handle copy data - No data loss
# ================================
d = {"a": 1, "b": 2, "c": 1}
inverted = {}

for k, v in d.items():
    # If the value (1) isn't in our new dict, create an empty list
    # Then append the key ('a') to that list
    inverted.setdefault(v, []).append(k)

print(inverted) 
# Output: {1: ['a', 'c'], 2: ['b']}