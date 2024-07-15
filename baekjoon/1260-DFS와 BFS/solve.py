import sys
from collections import deque


def init_graph(m):
    graph = dict()

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())

        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]

    for key in graph:
        graph[key].sort()

    return graph


def bfs(graph, start_node):
    visited = list()
    queue = deque()

    queue.append(start_node)
    while queue:
        node = queue.popleft()
        if node not in graph:
            visited.append(node)
            break
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


def dfs(graph, start_node):
    visited = list()
    stack = list()

    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in graph:
            visited.append(node)
            break
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited


n, m, v = map(int, sys.stdin.readline().strip().split())
graph = init_graph(m)

print(*dfs(graph, v))
print(*bfs(graph, v))
