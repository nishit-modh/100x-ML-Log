#Take a 3-digit integer from the user (e.g., 384) and calculate the sum of its digits (3 + 8 + 4 = 15) using only % and //. No strings allowed!
num = int(input("Enter a 3 digit number: "))
sum = 0
sum += num%10
num //= 10
sum += num%10
num //= 10
sum += num%10
print(sum)# Will be easy with loops