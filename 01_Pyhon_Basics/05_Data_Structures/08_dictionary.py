# --- MAPPING STRUCTURE (key–value storage) ---
# dict → Hash table mapping keys to values for fast lookup

student = {"name": "Rahul", "age": 20, "maths": 80}
print(student)

classroom = {
    "name": ["Hiren", "Viren", "Priten"],
    "age": [21, 22, 20],
    "marks": [78, 87, 69],
}
print(classroom)

# to add
classroom["grade"] = ["A", "B", "C"]
print(classroom)
