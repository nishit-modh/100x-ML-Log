# =========================================================
# PYTHON STRING METHODS DEMO
# Strings are IMMUTABLE → methods return a NEW string
# =========================================================

human = "I am NoT HumAn"

# =========================================================
# 1. CASE CONVERSION METHODS
# =========================================================

# upper() → converts all characters to UPPERCASE
print("Uppercase:", human.upper())

# lower() → converts all characters to lowercase
print("Lowercase:", human.lower())

# title() → Capitalizes first letter of each word
print("Title Case:", human.title())

# capitalize() → Capitalizes only the first letter
print("Capitalized:", human.capitalize())

print("====================================")


# =========================================================
# 2. PRACTICAL USE CASE (USER INPUT STANDARDIZATION)
# =========================================================

user_inp = input("Did you pass the exam (yes/no): ")

# convert to uppercase to avoid case mismatch
user_inp = user_inp.upper()

if user_inp == "YES":
    print("Congratulations!!!")
elif user_inp == "NO":
    print("Better luck next time.")
else:
    print("Invalid Input")

print("====================================")


# =========================================================
# 3. SPACE REMOVAL METHODS
# =========================================================

human = "      I Am Not Human      "

# strip() → removes spaces from BOTH sides
print(f"strip():  |{human.strip()}|")

# lstrip() → removes spaces from LEFT side
print(f"lstrip(): |{human.lstrip()}|")

# rstrip() → removes spaces from RIGHT side
print(f"rstrip(): |{human.rstrip()}|")

print("====================================")


# =========================================================
# 4. REPLACING TEXT
# =========================================================

fact = "I work with Javascript"

# Python strings are CASE-SENSITIVE
print(fact.replace("javascript", "Python"))   # not replaced
print(fact.replace("Javascript", "Python"))   # replaced correctly

# If substring is not found → original string returned
print(fact.replace("random_word", "Python"))

print("====================================")


# =========================================================
# 5. CHECKING STRING START / END
# =========================================================

link = "https://www.google.com"

# startswith() → returns True or False
if link.startswith("https"):
    print("Secure website")
else:
    print("Not secure")

# endswith() → checks ending pattern
print("Is it a .com site?", link.endswith(".com"))

print("====================================")


# =========================================================
# 6. SEARCHING INSIDE STRINGS
# =========================================================

text = "Python is powerful"

# find() → returns index of substring
print("Index of 'powerful':", text.find("powerful"))

# count() → counts occurrences
sentence = "python python python"
print("Count of 'python':", sentence.count("python"))

print("====================================")


# =========================================================
# 7. SPLITTING STRINGS
# =========================================================

data = "apple,banana,mango"

# split() → converts string into list
fruits = data.split(",")

print("Split result:", fruits)
print("First fruit:", fruits[0])

print("====================================")


# =========================================================
# 8. JOINING STRINGS
# =========================================================

words = ["Learn", "Python", "Today"]

# join() → combines list into string
sentence = " ".join(words)

print("Joined sentence:", sentence)

print("====================================")