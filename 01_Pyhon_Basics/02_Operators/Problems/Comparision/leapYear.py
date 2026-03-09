# Take a year (e.g., 2024) as input. Print True if it's a leap year and False if it isn't.
year = int(input("Enter year to check Leap year: "))
is_leap = (year % 400 == 0) + ((year % 4 == 0) * (year % 100 != 0))

print(
    "Is it a leap year: ",
    is_leap > 0,
)

"""
Pure Math: It relies entirely on the fact that True * True = 1 and True * False = 0.
This recreate logical operator functions without using logical operators.
"""
