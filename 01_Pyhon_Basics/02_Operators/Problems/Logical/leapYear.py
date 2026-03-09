# Write the leap year check using and and or.
year = int(input("Enter to check leap year: "))
print("Leap year: ", (year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
