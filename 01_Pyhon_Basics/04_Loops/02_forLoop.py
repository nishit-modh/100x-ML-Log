# for loop

print("------1 to 5------")
for i in range(1,6):
    print(i)

print("------10 to 1------")
for i in range(10,0,-1):
    print(i)

print("------5 times loop with number------")
for i in range(1,6):
    print(f"Loop: {i}")

print("=====1 to 10 and their sum=====")
total = 0
for i in range(1,11):
    print(i)
    total+=i
print("==Sum== :", total)