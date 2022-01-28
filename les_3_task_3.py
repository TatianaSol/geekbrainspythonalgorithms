# Урок 3. Задание 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

i = random.randint(10, 30)
arr = [random.randint(0, 100) for _ in range(i)]
imin = imax = 0

for i in range(i):
    if arr[i] > arr[imax]:
        imax = i
    elif arr[i] < arr[imin]:
        imin = i

print(f'Изначальный массив: {arr}')
arr[imax], arr[imin] = arr[imin], arr[imax]
print(f'Поменяли местами min ({arr[imax]}) и max ({arr[imin]}) элементы: {arr}')
