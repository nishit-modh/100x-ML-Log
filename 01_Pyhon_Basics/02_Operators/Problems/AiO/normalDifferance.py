"""
2. The Normalized Difference
Take two float inputs, f1 and f2.
Calculate their absolute difference (you can use "(f1 - f2)**2 ** 0.5" to get the absolute value without using abs()).
Check if this difference is less than 10% of the first number f1.
Print the boolean result.
"""

f1 = float(input("enter a float value: "))
f2 = float(input("enter a float value: "))
abs_diff = ((f1 - f2) ** 2)**0.5  # for absolute difference - abs(f1 - f2)

print(abs_diff < (f1 / 10))
