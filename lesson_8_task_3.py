# Урок 8. Задание 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
import random

n = int(input('Введите количество вершин: '))

print('Список смежности:')
graph = {j: {random.randint(0, n-1) for i in range(random.randint(0, n))} for j in range(n)}
print(graph)

visited = set()


def dfs(v):
    if v in visited:
        return
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            dfs(i)
    return visited


start = int(input('Введите вершину, с которой начнем обход: '))
print(dfs(start))
