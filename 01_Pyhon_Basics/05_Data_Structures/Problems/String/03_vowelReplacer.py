# 3. THE VOWEL REPLACER
# Problem: Replace every vowel (a, e, i, o, u) in a string with its 
# numerical position in the alphabet (a=1, e=5, i=9, o=15, u=21).
# Input: "apple"
# Output: "1ppl5"

# Default - NO MATH - method
s = input("String: ")
new_s =""
for char in s:
    if char not in "aeiouAEIOU":
        new_s += char
    else:
        if char == "a" or char == "A":
            new_s += "1"
        elif char == "e" or char == "E":
            new_s += "5"
        elif char == "i" or char == "I":
            new_s += "9"
        elif char == "o" or char == "O":
            new_s += "15"
        elif char == "u" or char == "U":
            new_s += "21"
print(f"Vowel replaced {s} using loop: {new_s}")

# MATH WAY
s = input("String: ")
new_s =""
for char in s:
    if char not in "aeiouAEIOU":
        new_s += char
    else:
        # Gives position value --> a = 1 using ASCII
        if char.islower():
            value = ord(char) - 96
        else:
            value = ord(char) - 64
        new_s += str(value)
print(f"Vowel replaced {s} using ASSII: {new_s}")


# ========================================
# Most Efficient - uses Map
# ========================================
vowel_map = {
    'a': '1', 'A': '1', 
    'e': '5', 'E': '5', 
    'i': '9', 'I': '9', 
    'o': '15', 'O': '15', 
    'u': '21', 'U': '21'
}

s = input("String: ")
new_s = ""
for char in s:
    # .get() looks for the char; if not found, it returns the char itself
    new_s += vowel_map.get(char, char)
print(new_s)