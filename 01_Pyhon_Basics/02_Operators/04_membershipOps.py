# Membership Operators
#"in" "not in"
#checks either given element is a part of other element

# in
access_allowed = ["admin", "manager", "employee"]
user = str(input("Enetr your role: "))
print("Access allowed: ", user in access_allowed)

# not in
blocked_user = ["Priten", "Dhruvil", "Vishwa"]
user_id = input("Enter your user Id: ")
print("Access: ", user_id not in blocked_user)

# works also on string
fact = "I am Nishit & I am Great"
check = input("Enter the match you want to check: ")
print("Is there a match? : ",check in fact)