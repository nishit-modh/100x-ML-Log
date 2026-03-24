# 9. NESTED FLATTERNER 🤯
# Problem: Convert a nested dictionary into a single-level dictionary
# where keys are joined by a dot.
# Example: d = {"user": {"name": "Amit", "info": {"age": 25}}}
# Output: {"user.name": "Amit", "user.info.age": 25}

d = {"user": {"name": "Amit", "info": {"age": 25}}}
flat_dict = dict()

stack_list = [(d, "")]


while stack_list:
    current_item , prefix = stack_list.pop()
    for k, v in current_item.items():
        new_prefix = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            stack_list.append((v,new_prefix))
        else:
            flat_dict[new_prefix] = v
print(flat_dict)