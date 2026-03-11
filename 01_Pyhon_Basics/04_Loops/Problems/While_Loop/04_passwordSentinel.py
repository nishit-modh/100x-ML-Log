# 4. THE PASSWORD SENTINEL
# Keep asking the user to enter a password until they match a pre-defined 
# secret string (e.g., "Admin@123"). Print "Access Granted" upon success.

password = "Admin@123"
while True:
    user_pass = str(input("Enter your password: "))
    if user_pass == password:
        print("Access Granted!")
        break
    else:
        print("Wrong password, Try Again!")