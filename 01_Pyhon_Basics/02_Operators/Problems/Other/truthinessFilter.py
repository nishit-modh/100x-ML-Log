"""
In AI, an empty string or the number 0 is often "False" (missing data).
Take an input from the user. Print True if the user actually typed something and False if they just pressed Enter.
"""
truthiness = bool(input("Are you a human: "))
print(truthiness)