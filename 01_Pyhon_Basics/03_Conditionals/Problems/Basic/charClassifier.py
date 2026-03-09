"""
2. Character Classifier
Take a single character as input. Use if/elif/else and string methods like .isupper(), .islower(), and .isdigit() to classify it as:
Uppercase Letter
Lowercase Letter
Digit
Special Character
"""
char = input("Enter simgle character: ")
if char.isupper():
    print("Uppercase character")
elif char.islower():
    print("Lowercase element")
elif char.isdigit():
    print("Digit element")
else:
    print("Special element")