# Задача номер 1

import random
n = int(input('Количество монет: '))
polozhenie = 0
count_1 = 0
count_2 = 0
for i in range(n):
    polozhenie = random.randint(1, 2)
    print(polozhenie, end=" ")
    if polozhenie < 2:
        count_1 += 1
    elif polozhenie > 1:
        count_2 += 1
print(f"\nГербом положений = {count_1},решкой положений = {count_2}.")
if count_1 > count_2:
    print(f"\nНужно перевернуть все положения, где решки")
elif count_2 > count_1:
    print(f"\nНужно перевернуть все положения, где герб")
else:
    print("Количество положений гербом и решкой одинаково")
