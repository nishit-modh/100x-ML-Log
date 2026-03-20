# 6. DICTIONARY MERGE-SUM
# Problem: Merge two dictionaries. If a key exists in both, sum their values.
# Example: d1 = {"a": 1, "b": 2}, d2 = {"b": 3, "c": 4} 
# Output: {"a": 1, "b": 5, "c": 4}

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# 1. Start with a copy of d1
result = d1.copy()

# 2. Only loop through d2 once
for key, value in d2.items():
    if key in result:
        result[key] += value  # Sum if key exists
    else:
        result[key] = value   # Add if key is new

print(result)