# Урок 9. Задание 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter
from operator import itemgetter


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code, value):
        self.left.walk(code, value + ['0'])
        self.right.walk(code, value + ['1'])


class Leaf:
    def __init__(self, char):
        self.char = char

    def walk(self, code, value):
        code[self.char] = ''.join(value)


def _make_leaves(obj: str):
    new_counted = {}
    for key, val in dict(Counter(obj)).items():
        new_counted[Leaf(key)] = val
    return list(new_counted.items())


def huff_encode(string_):
    items = _make_leaves(string_)
    while len(items) >= 2:
        left_leaf = items.pop()
        right_leaf = items.pop()
        leaf_count = left_leaf[1] + right_leaf[1]
        items.append((MyNode(left=left_leaf[0], right=right_leaf[0]), leaf_count))
        items.sort(key=itemgetter(1), reverse=True)
    _node = items.pop()[0]
    code = {}
    coded_string = ''
    _node.walk(code, [])
    for i in string_:
        coded_string += code[i]
    return code, coded_string


string = input('Введите строку: ')
print(f'Кодируем символы по методу Хаффмана: {huff_encode(string)[0]}')
print(f'Кодируем строку по методу Хаффмана: {huff_encode(string)[1]}')
