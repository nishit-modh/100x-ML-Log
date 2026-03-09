# Take two inputs: username and password.
# Print True only if BOTH fields are not empty.
username = str(input("Enter username: "))
password = str(input("Enter password: "))
has_username = bool(username)
has_password = bool(password)
print("Valid input: ", has_username != 0 and has_password != 0)