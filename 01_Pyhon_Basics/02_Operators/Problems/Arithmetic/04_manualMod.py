#Take two numbers, $a$ and $b$. Calculate the remainder of $a/b$ without using the % operator.
devidend = int(input("Enetr the Devidend: "))
devisor = int(input("Enetr the Devisor: "))
quotient = devidend//devisor
modulo = devidend - (devisor * quotient)
print(modulo)