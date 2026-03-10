# Pass - a null operation that serves as a placeholder where a statement is syntactically required but no action is needed.
# You primarily use pass to maintain a valid code structure when the actual implementation is pending


# Empty Functions/Methods:
def calculate_discount(price):
    pass  # todo : Implement discount logic later


# Empty Classes:
class InsufficientChocolateException(Exception):
    pass


# Conditional Statements:
value = 50
if value < 0:
    print("Negative value")
elif value > 0:
    print("Positive value")
else:
    pass # No action needed for zero

# Loops:
for num in range(5):
    if num == 2:
        pass # Does nothing when i is 2
    print(num) # Prints 0, 1, 2, 3, 4