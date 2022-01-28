# Урок 5. Задание 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.

from collections import deque

a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

def sum_hex(x, y):
    convert = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0
    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
    while x:
        if y:
            res = convert[x.pop()] + convert[y.pop()] + transfer
        else:
            res = convert[x.pop()] + transfer
        transfer = 0
        if res < 16:
            result.appendleft(convert[res])
        else:
            result.appendleft(convert[res - 16])
            transfer = 1
    if transfer:
        result.appendleft('1')
    return list(result)

def mult_hex(x, y):
    convert = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    spam = deque([deque() for _ in range(len(y))])
    x, y = x.copy(), deque(y)
    for i in range(len(y)):
        m = convert[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * convert[x[j]])
        for _ in range(i):
            spam[i].append(0)
    transfer = 0
    for _ in range(len(spam[-1])):
        res = transfer
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()
        if res < 16:
            result.appendleft(convert[res])
        else:
            result.appendleft(convert[res % 16])
            transfer = res // 16
    if transfer:
            result.appendleft(convert[transfer])
    return list(result)

print(f'Сумма чисел: {sum_hex(a, b)}')
print(f'Произведение чисел: {mult_hex(a, b)}')
