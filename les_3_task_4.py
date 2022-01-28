# Урок 3. Задание 4. Определить, какое число в массиве встречается чаще всего.

import random

i = random.randint(10, 30)
arr = [random.randint(0, 100) for _ in range(i)]
number = max_number = item = 0

for i in range(i):
    for k in range(i):
        if arr[i] == arr[k]:
            number += 1
    if number > max_number:
        max_number = number
        item = arr[i]

print(f'Массив: {arr}')
if max_number == 0:
    print('Все числа уникальны')
else:
    print(f'Число {item} встречается {max_number} раз')
