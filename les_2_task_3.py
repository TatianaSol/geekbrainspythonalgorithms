# Урок 2. Задание 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num = int(input('Введите целое число: '))
num2 = ''

while num > 0:
    num2 += str(num % 10)
    num //= 10

print(f'Ваше число наоборот: {num2}')
