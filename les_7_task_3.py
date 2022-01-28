# Урок 7. Задание 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random

n = 15
list = [random.randint(0, 100) for _ in range(n)]
print(f'Изначальный массив: {list}')


def median(array):
    if len(array) % 2 == 1:
        return select(array, len(array) / 2)
    else:
        return (select(array, len(array) / 2 - 1) + select(array, len(array) / 2)) / 2


def select(array, k):
    if len(array) == 1:
        return array[0]
    pivot = random.choice(array)
    less = [item for item in array if item < pivot]
    more = [item for item in array if item > pivot]
    pivots = [item for item in array if item == pivot]
    if k < len(less):
        return select(less, k)
    elif k < len(less) + len(pivots):
        return pivots[0]
    else:
        return select(more, k - len(less) - len(pivots))


print(f'Медиана: {median(list)}')
