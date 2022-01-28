# Урок 9. Задание 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * задача считается решённой, если в коде использована функция вычисления хеша (hash(), sha1() или любая другая из модуля hashlib)
import hashlib


def substring(string):
    if len(string) == 0 or len(string) == 1:
        return len(string)
    hash_list = set()
    step = 1
    while step < len(string):
        for i in range(len(string)):
            hash_var = hashlib.sha1(string[i:i + step].encode('utf-8')).hexdigest()
            hash_list.add(hash_var)
        step += 1
    return len(hash_list)


str = input('Введите строку: ')
print(f'Число подстрок в строке: {substring(str)}')
