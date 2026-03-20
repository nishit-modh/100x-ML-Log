# 3. SELECTIVE PURGE
# Problem: Remove all keys from a dictionary whose values are less than 'k'.
# Example: d = {"a": 10, "b": 50, "c": 5}, k = 20 -> Output: {"b": 50}

# perfect in 1st attempt
d = {"a": 10, "b": 50, "c": 5}
k = int(input("Filter for LT k: "))

new_dict = {key : value for key,value in d.items() if value >= k}
print(new_dict)