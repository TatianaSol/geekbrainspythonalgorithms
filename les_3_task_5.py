# Урок 3. Задание 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

i = random.randint(10, 30)
arr = [random.randint(-100, 100) for _ in range(i)]

for i in range(i):
    if arr[i] < 0:
       index = i
       arr[index] = arr[i]

for i in range(i):
    if arr[index] < arr[i] < 0:
        arr[index] = arr[i]
        index = i

print(f'Массив: {arr}')
print(f'Максимальный отрицательный элемент: {arr[index]} на позиции {index}')
