# 6. THE POWER CALCULATOR (MANUAL)
# Take a Base and an Exponent. Calculate the result using only a while loop.
# Do not use the ** operator or any built-in power functions.

N = int(input("Enter integer N as a base: "))
P = int(input("Enter integer P as a power: "))
og_N = N
og_P = P

while P > 1:
    N *= og_N
    P -= 1
print(f"{og_N} power {og_P} = {N}")

# Efficient, Clean and edgecase inclusive version - (p = 0)
"""
base = int(input("Base: "))
power = int(input("Power: "))
result = 1
count = power

while count > 0:
    result *= base
    count -= 1

print(f"{base}^{power} = {result}")
"""