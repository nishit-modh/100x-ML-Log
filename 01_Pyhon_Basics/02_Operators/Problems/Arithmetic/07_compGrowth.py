# Write a formula to calculate the final amount after 5 years for a Principal $P$, given an annual interest rate $r$, compounded annually: $A = P(1 + r)^t$.
principal = int(input("Enter principal amount: "))
rate = float(input("Enter rate of Interest: ")) / 100
duration = int(input("Enter time duration: "))
comp_interest = principal * (1 + rate) ** duration
print(f"Earned Compound interest is: {round(comp_interest - principal)}")
# "round" method rounds the float to closest integer
print(f"Final collected amount is: {comp_interest}")
