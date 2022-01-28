# Урок 4. Задание 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import cProfile
n = 1555

# ВАРИАНТ №1. Решето Эратосфена

def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:
        for i in range(len(sieve)):
            if sieve[i] != 0:
                count += 1
                if count == n:
                    return sieve[i]
                j = i + sieve[i]
                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]
        prime.extend([i for i in sieve if i != 0])
        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]
        for i in range(len(sieve)):
            for num in prime:
                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break

cProfile.run('eratosthenes_sieve(n)')

# ВАРИАНТ №2. Без Решета Эратосфена

def search_prime(n):
   count = 1
   number = 1
   prime = [2]

   if n == 1:
       return 2
   while count != n:
       number += 2
       for num in prime:
           if number % num == 0:
               break
       else:
           count += 1
           prime.append(number)
   return number

cProfile.run('search_prime(n)')

# РЕЗУЛЬТАТЫ ОЦЕНКИ АЛГОРИТМОВ

# ВАРИАНТ №1. Поиск N=1555 по счету простого числа по алгоритму Решето Эратосфена занял  0.218 секунд
# 6867 function calls in 0.218 seconds
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.218    0.218 <string>:1(<module>)
#        1    0.213    0.213    0.218    0.218 les_4_task_2.py:16(eratosthenes_sieve)
#        1    0.001    0.001    0.001    0.001 les_4_task_2.py:21(<listcomp>)
#        3    0.001    0.000    0.001    0.000 les_4_task_2.py:37(<listcomp>)
#        3    0.002    0.001    0.002    0.001 les_4_task_2.py:39(<listcomp>)
#        1    0.000    0.000    0.218    0.218 {built-in method builtins.exec}
#     6853    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

# ВАРИАНТ №2. Поиск N=1555 по счету простого числа без алгоритма Решето Эратосфена занял  0.154 секунд
# 1558 function calls in 0.154 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.154    0.154 <string>:1(<module>)
#         1    0.154    0.154    0.154    0.154 les_4_task_2.py:49(search_prime)
#         1    0.000    0.000    0.154    0.154 {built-in method builtins.exec}
#      1554    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ВАРИАНТ №2 более предпочтителен, так как быстрее выполняет запрос, что объясняется тем, что функция append вызывается
# только при нахождении простого числа (по итогу вызовется N-1 раз), а в ВАРИАНТЕ №1 функция len вызывается при проверке КАЖДОГО числа
# от 2 до N-го простого, что увеличивает время работы алгоритма.