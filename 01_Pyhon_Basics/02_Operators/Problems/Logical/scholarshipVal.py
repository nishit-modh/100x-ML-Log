"""
A student gets a scholarship if:
- (GPA > 3.8 and Attendance > 90)
- OR (GPA > 3.5 and is_captain == True)
"""

gpa = float(input("Enter your grades: "))
captain = str(input("Are you a captain(T/F): "))
is_captain = captain == "T"
attendance = int(input("Enter attendance percentage: "))

print(
    "Will you get scholarship?: ",
    (gpa > 3.8 and attendance > 90) or (gpa > 3.5 and is_captain),
)
