# Урок 3. Задание 4. Определить, какое число в массиве встречается чаще всего.

import cProfile
import random

# ВАРИАНТ №1

def variant1():
    i = 10000
    arr = [random.randint(0, 100) for _ in range(i)]
    number = max_number = item = 0
    for i in range(i):
        for k in range(i):
            if arr[i] == arr[k]:
                number += 1
        if number > max_number:
            max_number = number
            item = arr[i]
    return item, max_number

cProfile.run('variant1()')

# ВАРИАНТ №2

def variant2():
    i = 10000
    array = [random.randint(0, 100) for _ in range(i)]
    array_set = set(array)
    most_common = None
    qty_most_common = 0
    for item in array_set:
        qty = array.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item
    return item, qty_most_common

cProfile.run('variant2()')

# ВАРИАНТ 3

def variant3():
    i = 10000
    array = [random.randint(0, 100) for _ in range(i)]
    diction = {}
    for item in array:
        if item in diction.keys():
            diction[item] += 1
    return item

cProfile.run('variant3()')

# РЕЗУЛЬТАТЫ ОЦЕНКИ АЛГОРИТМОВ

# ВАРИАНТ №1 при длине массива i=10000 алгоритм выполняется за 9.630 секунды
# 52660 function calls in 9.630 seconds
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    9.630    9.630 <string>:1(<module>)
#       1    9.581    9.581    9.630    9.630 les_4_task_1.py:7(variant1)
#       1    0.006    0.006    0.049    0.049 les_4_task_1.py:9(<listcomp>)
#   10000    0.020    0.000    0.037    0.000 random.py:174(randrange)
#   10000    0.007    0.000    0.044    0.000 random.py:218(randint)
#   10000    0.012    0.000    0.017    0.000 random.py:224(_randbelow)
#       1    0.000    0.000    9.630    9.630 {built-in method builtins.exec}
#   10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   12655    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}

# ВАРИАНТ №2 при длине массива i=10000 алгоритм выполняется за 0.081 секунды
# 52754 function calls in 0.081 seconds
#   calls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.081    0.081 <string>:1(<module>)
#       1    0.000    0.000    0.081    0.081 les_4_task_1.py:24(variant2)
#       1    0.006    0.006    0.044    0.044 les_4_task_1.py:26(<listcomp>)
#   10000    0.015    0.000    0.032    0.000 random.py:174(randrange)
#   10000    0.006    0.000    0.038    0.000 random.py:218(randint)
#   10000    0.013    0.000    0.017    0.000 random.py:224(_randbelow)
#       1    0.000    0.000    0.081    0.081 {built-in method builtins.exec}
#   10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#     101    0.036    0.000    0.036    0.000 {method 'count' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   12648    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}

# ВАРИАНТ №3 при длине массива i=10000 алгоритм выполняется за 0.052 секунды
# 62722 function calls in 0.052 seconds
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.052    0.052 <string>:1(<module>)
#       1    0.003    0.003    0.052    0.052 les_4_task_1.py:42(variant3)
#       1    0.006    0.006    0.048    0.048 les_4_task_1.py:44(<listcomp>)
#   10000    0.017    0.000    0.035    0.000 random.py:174(randrange)
#   10000    0.006    0.000    0.042    0.000 random.py:218(randint)
#   10000    0.013    0.000    0.019    0.000 random.py:224(_randbelow)
#       1    0.000    0.000    0.052    0.052 {built-in method builtins.exec}
#   10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   12717    0.004    0.000    0.004    0.000 {method 'getrandbits' of '_random.Random' objects}
#   10000    0.001    0.000    0.001    0.000 {method 'keys' of 'dict' objects}

# ВАРИАНТ №3 (с использованием словаря) самый быстрый,
# ВАРИАНТ №2 с испльзование функции count - немного медленней первого варианта,
# ВАРИАНТ №1 с использованием циклов - самый медленный, значительно медленнее первых двух вариантов,
# использующих встроенные функции поиска в словарях и списках.
# Лучший вариант - ВАРИАНТ №3 - самый быстрый и создает наименьшее количество перменных в процессе.