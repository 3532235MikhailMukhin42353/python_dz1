# задача 1
def stepen(num_one, num_two):
    if num_two == 1:
        return num_one
    if num_two != 1:
        return num_one * stepen(num_one, num_two-1)


num_one = int(input('Число: '))
num_two = int(input('Степень: '))
print(stepen(num_one, num_two))
