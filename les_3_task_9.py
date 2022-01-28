# Урок 3. Задание 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

min_column = matrix[0]

for line in matrix:
    for i, item in enumerate(line):
        if item < min_column[i]:
            min_column[i] = item

print('Минимальные элементы столбцов матрицы:')
print(min_column)

max_in_min = min_column[0]

for i in range(0, len(min_column)):
    if min_column[i] > max_in_min:
        max_in_min = min_column[i]

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_in_min}')
