# Урок 3. Задание 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

i = random.randint(10, 30)
arr = [random.randint(0, 100) for _ in range(i)]
imin = imax = sum = 0

for i in range(i):
    if arr[i] > arr[imax]:
        imax = i
    elif arr[i] < arr[imin]:
        imin = i

if imin < imax:
    for i in range(imin + 1, imax):
        sum += arr[i]
else:
    for i in range(imax + 1, imin):
        sum += arr[i]

print(f'Массив: {arr}')
print(f'Сумма элементов, находящихся между min ({arr[imin]}) и max ({arr[imax]}) элементами: {sum}')
