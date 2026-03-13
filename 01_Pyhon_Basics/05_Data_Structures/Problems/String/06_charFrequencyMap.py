# 6. THE CHARACTER FREQUENCY MAP
# Problem: Count the frequency of every character in a string and 
# display it without using the .count() method.
# Input: "banana"
# Output: b: 1, a: 3, n: 2

s = input("String: ")
repeat = ""
for char in s:
    if char not in repeat:
        repeat += char
        count = 0
        for i in s:
            if char == i:
                count +=1
        print(f"{char}: {count} ", end="")


print()
# Shortcut using count() 
repeat = ""
for char in s:
    if char not in repeat:
        print (f"{char}: {s.count(char)}", end=" ")
        repeat += char