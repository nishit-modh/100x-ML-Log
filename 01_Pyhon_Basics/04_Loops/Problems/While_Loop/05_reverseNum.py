# 5. THE REVERSE NUMBER CONSTRUCTER
# Take an integer N. Use math to reverse the digits. !!! HINT: (modulo and floor division) !!!
# Example: Input 123 -> Output 321.

N = int(input("Enter an Integer: "))
if N < 1:
    print("Enter a Positive integer: ")
else:
    reverse = 0
    og_N = N
    while N > 0:
        last_digit = N % 10
        reverse =  reverse * 10 + last_digit 
        N //= 10
    if og_N == reverse:
        print(f"It is a plindrome number: reverse of {og_N} is it self.")
    else:
        print(f"Reverse of the {og_N} is {reverse}")
        