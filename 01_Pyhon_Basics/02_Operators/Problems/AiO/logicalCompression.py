"""
4. The Logical Compression
Take a 4-digit integer year.
Create a single boolean variable check that is True if:
The year is even AND (it ends in 00 OR is greater than 2024).
Note: Do not use if or and/or/not. Use the boolean arithmetic (+, *) and comparisons only.
"""
year = int(input("Enter the year: "))
check = (year%2 ==0) * ((year%100 == 0) + (year > 2024) > 0)
print(check)