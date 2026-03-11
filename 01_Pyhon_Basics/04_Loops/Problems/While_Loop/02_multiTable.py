# 2. THE MULTIPLICATION TABLE
# Take an integer N. Use a while loop to print its multiplication table from 1 to 10.
# Format: "N x i = Result"

N = int(input("Enter a nuber to get a Table: "))
if N < 1:
    print("Enter a positive Integer!")
else:
    i = 1
    while i <= 10:
        print(f"{N} X {i} = {N*i}")
        i += 1