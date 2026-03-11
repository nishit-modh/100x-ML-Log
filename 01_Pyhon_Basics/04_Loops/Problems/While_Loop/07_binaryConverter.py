# 7. THE BINARY CONVERTER
# Take a decimal integer N. Use a while loop to find its binary (Base-2) 
# representation by repeatedly dividing by 2 and tracking remainders.

N = int(input("Convert Binary: "))
og_N = N
if N < 0:
    print("Invalid Input.")
elif N == 0:
    binary = "0"
else:
    binary = ""
    while N > 0:
        binary = str(N%2) + binary # doing this we'll geta reversed string - correct (cause we want reverse)
        N //= 2
print(f"Binary of {og_N} is {binary}")