# 12. LRU CACHE (MINI SIMULATION) 🤯
# Problem: Keep a dictionary of size 'N'. When you add a new item and the
# dictionary is full, remove the LEAST RECENTLY USED (the oldest) item.
# Example: Capacity 2. Put(1,1), Put(2,2), Get(1), Put(3,3).
# Result: Key 2 is removed because 1 was recently accessed.


# ===========================================
# Manual way - 1st attempt (Partially functional but incorrect and manual)
# ===========================================

# N = 3
# cache = {1: "alpha", 2: "beta", 3: "gamma"}

# lru = 1
# next_lru = [2, 3]
# ele_number = N


# want_access = input("Want to access cache elements? (y/n): ")
# if want_access == "y":
#     while True:
#         print("Action to perform : ")
#         print("n - for new entry")
#         print("a - for accessing element ")
#         print("q - for exit")
#         action = input("Action: ")
#         if action == "q":
#             print("loop exit: ")
#             print(f"Current cache: {cache}")
#             break
#         elif action == "n":
#             add = input("Enter element to add: ")
#             current_N = len(cache)
#             if current_N < N:
#                 cache[current_N + 1] = add
#                 print(add, "added")
#                 break
#             else:
#                 ele_number += 1
#                 cache.pop(lru, None)
#                 cache[ele_number] = add
#                 lru = next_lru.pop(0)
#                 next_lru.append(ele_number)
#         elif action == "a":
#             access = int(input("Enter element to access: "))
#             print(cache[access]) if access in cache else print("Not Present!")
#             next_lru.append(lru)
#             lru = next_lru.pop(0)
#         else:
#             print("Invalid input.")


# ===========================================
# using pop() in dictionary - 
# ===========================================
# =========================================================
# 12. LRU CACHE SIMULATION (FINAL VERSION)
# =========================================================

cache = {"1st": "alpha", "2nd": "beta", "3rd": "gamma"}
N = 3

while True:
    print(f"\n--- Cache Status: {list(cache.keys())} ---")
    action = input("Action (n: new/update, a: access, q: quit): ").lower()

    if action == "q":
        break

    elif action == "n":
        key = input("Enter key: ")
        val = input("Enter value: ")
        
        # LOGIC: If key exists, remove it first to "reset" position
        if key in cache:
            cache.pop(key)
        # If key is new AND cache is full, evict the oldest
        elif len(cache) >= N:
            oldest = next(iter(cache))
            cache.pop(oldest)
            print(f"Evicted: {oldest}")

        cache[key] = val
        print(f"Stored: {key}")

    elif action == "a":
        key = input("Enter key to access: ")
        if key in cache:
            # THE "LRU SECRET": Pop and re-add to make it the NEWEST
            value = cache.pop(key)
            cache[key] = value
            print(f"Value: {value}")
        else:
            print("Error: Key not found!")

print(f"Final Cache State: {cache}")
