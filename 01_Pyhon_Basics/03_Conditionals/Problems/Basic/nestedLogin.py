"""
5. Nested Login System
Take username. If it is "admin":
Ask for password. If password is "python123", print "Access Granted".
If password is wrong, print "Wrong Password".
If username is not "admin", print "Unknown User".
"""

username = str(input("Enter username: "))
if username == "admin":
    password = str(input("Enter Password: "))
    if password == "123":
        print("access granted!!!")
    else:
        print("Wrong password!!!")
else:
    print("Unknown user!")
