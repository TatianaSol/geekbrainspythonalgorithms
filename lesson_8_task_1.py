# Урок 8. Задание 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было? Примечание. Решите задачу при помощи построения графа.

n = int(input('Введите количество друзей: '))

print('Для решения задачи построим неориентированный граф:')
graph = [[1 if i != j else 0 for j in range(n)] for i in range(n)]
print(*graph, sep='\n')

a = {frozenset([ci+1, ni+1]) for ni, ne in enumerate(graph) for ci, ce in enumerate(ne) if ce == 1}
handshake = len(a)

print(f'Количество рукопожатий равно количеству ребер в графе: {handshake}')
