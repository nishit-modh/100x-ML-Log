# Simploe Interest Calcualtor
principal = float(input("Enter Principal amount: "))
interest = float(input("Enter Interest rate: "))
duration = float(input("enter Time duration(in years): "))
simple_interest = (principal * interest * duration)/100
print(f"Total Simple Interest is : {simple_interest}")