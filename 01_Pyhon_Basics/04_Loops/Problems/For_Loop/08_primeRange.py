# 8. THE PRIME RANGE SCANNER
# Problem: Given an integer N, print ALL prime numbers between 2 and N.
# Example: Input: 10
# Output: 2 3 5 7

N = int(input("Enter a number: "))
for i in range(2, N+1):
    is_prime = True
    for j in range(2, (round(i**0.5)) + 1):# round to avoid math error : if sqrt of 4 => 1.9999 -> 2
        if i%j == 0:
            is_prime = False
    if is_prime:
        print(i)