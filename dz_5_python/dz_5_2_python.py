# задача 2
def summ(a, b):
    if a == 0:
        return b
    return summ(a-1, b+1)


number_1 = int(input('Первое число: '))
number_2 = int(input('Второе число: '))
print(summ(number_1, number_2))
