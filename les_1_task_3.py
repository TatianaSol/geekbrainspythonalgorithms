# Урок 1. Задание 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.

import random

num_start = input('Начало диапазона: ')
num_end = input('Конец диапазона: ')
choice = input('Введите номер действия:\n'
               '1. Случайное целое число\n'
               '2. Случайное вещественное число\n'
               '3. Случайный символ:\n')

if choice == '1':
    num_start, num_end = int(num_start), int(num_end)
    result = random.randint(num_start, num_end)
    print(f'Случайное целое число: {result}')
elif choice == '2':
    num_start, num_end = float(num_start), float(num_end)
    result = random.uniform(num_start, num_end)
    print(f'Случайное вещественное число: {result}')
elif choice == '3':
    num_start, num_end = ord(num_start), ord(num_end)
    result = chr(random.randint(num_start, num_end))
    print(f'СлучайнЫЙ символ: {result}')
else:
    print('Неизвестное действие')
