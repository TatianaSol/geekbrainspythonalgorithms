# Урок 6. Задание 1. 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Для анализа используется Урок 3. Задание 4. Определить, какое число в массиве встречается чаще всего.

import sys
import random

def show_size(x, level=0):
    result_size = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                result_size += show_size(key, level + 1)
                result_size += show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                result_size += show_size(item, level + 1)
    return result_size

# ВАРИАНТ №1

def variant1():
    i = 100
    arr = [random.randint(0, 100) for _ in range(i)]
    number = max_number = item = 0
    for i in range(i):
        for k in range(i):
            if arr[i] == arr[k]:
                number += 1
        if number > max_number:
            max_number = number
            item = arr[i]
    local_variables_dict = locals().copy()
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
         size_of_all_variables += show_size(local_variables_dict[var])
         print(f'Общий размер используемых переменных в функции {variant1.__name__}: {size_of_all_variables} байт')
    return item, max_number

print(f'Результат вызова функции: {variant1()}')

# ВАРИАНТ №2

def variant2():
    i = 100
    array = [random.randint(0, 100) for _ in range(i)]
    array_set = set(array)
    most_common = None
    qty_most_common = 0
    for item in array_set:
        qty = array.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item
    local_variables_dict = locals().copy()
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
         size_of_all_variables += show_size(local_variables_dict[var])
         print(f'Общий размер используемых переменных в функции {variant2.__name__}: {size_of_all_variables} байт')
    return item, qty_most_common

print(f'Результат вызова функции: {variant2()}')

# ВАРИАНТ 3

def variant3():
    i = 100
    array = [random.randint(0, 100) for _ in range(i)]
    diction = {}
    for item in array:
        if item in diction.keys():
            diction[item] += 1
    local_variables_dict = locals().copy()
    size_of_all_variables = 0
    for var in local_variables_dict.keys():
         size_of_all_variables += show_size(local_variables_dict[var])
         print(f'Общий размер используемых переменных в функции {variant3.__name__}: {size_of_all_variables} байт')
    return item

print(f'Результат вызова функции: {variant3()}')

# Python 3.7.6, Windows 7 64 bit
# Общий размер используемых переменных в функции variant1: 3852 байт. Результат вызова функции: (74, 50)
# Общий размер используемых переменных в функции variant2: 7832 байт. Результат вызова функции: (100, 5)
# Общий размер используемых переменных в функции variant3: 4004 байт. Результат вызова функции: 22
# Второй вариант использует вдвое больше памяти, чем другие варианты, из-за того, что создаваемый список переводит во вмножество для дальнейшей работы, что ускоряет работу по сравнению с первым вариантом.
# Первый вариант создает список для поиска и использует всего три дополнительный переменных для работы, за счет чего является самым экономным в работе с памятью.
# Третий вариант создает список и затем из него генерирует словарь, избегая повторений, в целом, использует немного больше памяти, чем самый экономный первый вариант.
# Если выбирать только по объему используемой памяти, то первый вариант - самый оптимальный.# Если учитывать еще и скорость работы функции и вспомнить результаты проверок из Урока 4, то оптимальным вариантом по сочетанию времени и объему используемой памяти будет вариант 3.
