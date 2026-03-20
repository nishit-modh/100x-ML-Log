# 4. LEADERBOARD FINDER 👍
# Problem: Find the key that has the maximum value.
# Example: d = {"Amit": 88, "Riya": 92, "Sohan": 79} -> Output: "Riya"

#======================
# 1st attempt - 
#======================
d = {"Amit": 88, "Riya": 92, "Sohan": 79}
max_points = 0
topper = ""
for key, value in d.items():
    if value > max_points:
        max_points = value
        topper = key
print(f"Max point value is of: {topper}")

# ====================================
# using max() - shortcut
# ====================================
d = {"Amit": 88, "Riya": 92, "Sohan": 79}

# "Look at d, but for every key, use d.get to compare"
topper = max(d, key=d.get)

print(topper) # "Riya"