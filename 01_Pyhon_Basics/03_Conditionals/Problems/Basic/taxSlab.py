"""
🏛️ Challenge 3: The Professional Tax Slab
This one is about layered logic. You calculate tax only on the amount that falls within each bucket.

The Rules:
0 - 2.5L: 0% Tax
2.5L - 5L: 5% of the amount above 2.5L
5L - 10L: 10% of the amount above 5L + 12,500 (which is the tax from the previous bucket)
Above 10L: 20% of the amount above 10L + 62,500
"""

income = int(input("Enter your income: "))
if income <= 250000:
    print("Non-Taxble")
elif income <= 500000:
    print(f"Tax = {(income - 250000)*0.05}")
elif income <= 1000000:
    print(f"Tax = {((income - 500000)*0.1) + 12500}")
else:
    print(f"Tax = {((income - 1000000)*0.2) + 62500}")
