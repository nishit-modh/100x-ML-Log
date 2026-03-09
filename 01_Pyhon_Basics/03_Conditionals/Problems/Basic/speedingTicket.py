"""
7. Speeding Ticket
Take speed and a boolean is_birthday.
If speed <= 60: No ticket.
If speed is 61-80: "Small Ticket".
If speed > 80: "Big Ticket".
Special Rule: If it's your birthday, your speed can be 5 higher in all categories.
"""

speed = float(input("Enter your speed: "))
birthday = str(input("Is today your birthday(Y/N): "))
if birthday == "Y":
    speed -= 5

if speed <= 60:
    print("No ticket")
elif speed <= 80:
    print("Small ticket")
else:
    print("Hugeee ticket")
