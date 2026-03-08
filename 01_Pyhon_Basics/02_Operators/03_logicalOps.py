# Logical Operators
#"and" "or" "not"

# and Operator
citizen = True
age = int(input("Enter your age: "))
print("(and operation)Can vote: ",(citizen == True) and (age >= 18))

# or operator
marks = int(input("Enter test marks: "))
bands = float(input("Enter IELTS bands: "))
print("(or operation)Eligible for Application: ", (marks >= 35) or (bands > 6))

# not operator
human = True
print("(not operator)Is human: ",not human)