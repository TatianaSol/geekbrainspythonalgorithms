# Урок 1. Задание 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

letter1 = ord(input('Введите первую букву: ')) - ord('a') + 1
letter2 = ord(input('Введите вторую букву: ')) - ord('a') + 1

print(f'Порядковый номер 1ой буквы: {letter1}, 2ой буквы: {letter2}\n'
      f'Число букв между ними: {abs(letter1 - letter2) - 1}')
