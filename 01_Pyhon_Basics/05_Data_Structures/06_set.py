# --- SET STRUCTURES (unique element collections) ---
# set → Unordered collection storing unique elements
# removes duplicate values automatically

emails = {
    "wholt@gmail.com",  # dupe 1
    "kellynicholas@yahoo.com",
    "dlarsen@outlook.com",
    "deborahsullivan@hotmail.com",  # dupe 2
    "psmith@aol.com",
    "ukelley@icloud.com",
    "wholt@gmail.com",  # dupe 1
    "deborahsullivan@hotmail.com",  # dupe 2
}
print(emails)

# efficient way of set creation
nums = [1, 2, 3, 3, 4, 5, 6, 5, 6, 4, 9, 0, 5, 4, 2, 2]
s = set(nums)
print(f"Unique: {s} is a {type(s)}")


# ===================================
# frozenset   → Immutable version of set for fixed unique data
# ===================================
frozen_set = frozenset([1, 2, 3, 4, 5, 6, 7, 7, 8])
print(f"Frozen set: {frozen_set}")

# error - cause frozenset is immutable
# frozen_set.discard(999)
