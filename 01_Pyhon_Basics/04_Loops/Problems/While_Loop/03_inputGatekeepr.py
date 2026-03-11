# 3. THE INPUT GATEKEEPER & TOTALIZER
# Continuously ask the user for numbers. Keep adding them to a running total.
# Stop only when the user enters 0. Print the final sum and "Program Stopped".

total_sum = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    total_sum += num
print(f"Total sum: {total_sum}")