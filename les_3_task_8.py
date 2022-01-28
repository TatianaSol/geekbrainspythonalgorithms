# Урок 3. Задание 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = [[int(input('Введите число: ')) for _ in range(4)] for _ in range(4)]

print('В последнем столбце посчитана сумма по строкам, итоговая матрица: ')

for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += item
        print(f'{item:>4}', end='')
    print(f' {sum_line:>4}')