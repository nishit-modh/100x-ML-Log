# Take a float, multiply it by 100, and convert it to an integer. Explain why int(0.58 * 100) might sometimes give you 57 instead of 58 in programming (hint: floating-point binary).
# The Precision Trap
a = 0.58
b = a * 100 

# Why this happens:
# In binary, 0.58 is stored as 0.57999999999999996.
# Multiplying by 100 gives 57.999999999999996.

result_int = int(b)    # int() is 'greedy'—it just cuts off (truncates) decimals. Result: 57
result_round = round(b) # round() looks at the nearest whole number. Result: 58

print(f"Using int(): {result_int}")
print(f"Using round(): {result_round}")