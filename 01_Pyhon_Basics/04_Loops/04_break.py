# break - loop control statement used to immediately terminate the current for or while loop.
# In almost all cases - used inside if statement block

# The loop stops entirely when the number 3 is encountered.
for number in range(5):
    if number == 3:
        break
    print(f"Number is {number}") # 3 will not be printed

print("Out of loop - 3 is found - Loop is Broken")

print("==========")
# in while loop
i = 1
while i <= 20:
    print(i)
    i +=1
    if i == 7:
        print(f"{i}hala for a Reason!!! = {i}")
        break
