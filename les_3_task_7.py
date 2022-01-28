# Урок 3. Задание 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

i = random.randint(10, 30)
arr = [random.randint(0, 100) for _ in range(i)]
print(arr)

imin_1 = 0
imin_2 = 1

for i in range(i):
    if arr[imin_1] > arr[i]:
        imin_2 = imin_1
        imin_1 = i
    elif arr[imin_2] > arr[i]:
        imin_2 = i

print(f'Два наименьших элемента массива: {arr[imin_1]}, {arr[imin_2]}')
