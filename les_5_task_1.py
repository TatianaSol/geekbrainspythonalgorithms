# Урок 5. Задание 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

n = int(input('Введите количество предприятий: '))

enterprise = collections.defaultdict()
enterprise_profit = 0

for i in range(1, n+1):
    name = input(f'Введите название {i}го предприятия: ')
    company_profit = 0
    for q in range(1, 5):
        company_profit += float(input(f'Введите прибыль компании за {q}ый квартал: '))
    enterprise[name] = company_profit
    enterprise_profit += company_profit

average_profit = enterprise_profit / n
print(f'Средняя прибыль за год среди всех предприятий: {average_profit:.{2}f}')
print('Предприятия, чья прибыль выше среднего:', [name for name in enterprise if enterprise[name] > average_profit])
print('Предприятия, чья прибыль ниже среднего:', [name for name in enterprise if enterprise[name] < average_profit])
