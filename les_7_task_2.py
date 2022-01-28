# Урок 7. Задание 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

n = 10
array = [random.uniform(0, 50) for _ in range(n)]
print(f'Изначальный массив: {array}')


def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:] + b[j:]
    return result


def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        l = a[:len(a) // 2]
        r = a[len(a) // 2:]
    return merge(merge_sort(l), merge_sort(r))


print(f'Отсортированный массив: {merge_sort(array)}')
