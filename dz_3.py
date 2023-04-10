import math

bilet = int(input('Введите шестизначный номер билета: '))

x1 = math.floor(bilet / 100000)  # 1 --> 123456
x2 = math.floor(bilet / 10000)  # 12
x21 = x2 % 10  # 2
x3 = math.floor(bilet / 1000)  # 123
x31 = x3 % 10  # 3
x4 = math.floor(bilet / 100)  # 1234
x41 = x4 % 10  # 4
x5 = math.floor(bilet / 10)  # 12345
x51 = x5 % 10  # 5
x6 = bilet % 10  # 6
print(x1, x21, x31, x41, x51, x6)
sum_1 = x1 + x21 + x31
sum_2 = x41 + x51 + x6
print(f"Сумма первых чисел = {sum_1}, сумма последних = {sum_2}.")

if sum_1 == sum_2:
    print('Yes')
elif bilet > 999999:
    print('Ошибка ввода')
else:
    print('No')
