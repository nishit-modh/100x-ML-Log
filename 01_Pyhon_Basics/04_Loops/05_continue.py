# continue -  loop control mechanism that skips the remaining code in the current iteration and proceeds immediately to the next iteration of the loop
# use in for loop
for number in range(1, 6):
    if number % 2 == 0:
        continue  # Skip the rest of the code for this iteration - even nums skipped
    print(number)

print("==========")
# use in while loop
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the print statement for this iteration - skips where count == 3
    print(count)

print("==========")
# TO skip invalid values => negatives
weight = [40, -1, 50, -34, 56, -64, 78, 97, -103, 120, 86, -23, 20, -1000, 130]
for i in weight:
    if i < 0:
        continue
    print(i)