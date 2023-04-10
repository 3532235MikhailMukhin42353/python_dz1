import math

a = int(input('Введите трехзначное число: '))
x1 = math.floor(a / 100)  # 1
x2 = a % 10  # 3
x3 = a % 100
x4 = math.floor(x3 / 10)  # 2
sum = x1 + x2 + x4
print(sum)
print(x1, x2, x4)
