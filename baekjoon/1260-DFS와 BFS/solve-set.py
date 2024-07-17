import sys
from collections import deque
from collections import defaultdict


def init_graph(m):
    graph = defaultdict(list)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    for key in graph:
        graph[key].sort()

    return graph


def bfs(graph, start_node):
    visited = set()
    queue = deque()
    order = list()

    queue.append(start_node)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node])
    return order


def dfs(graph, start_node):
    visited = set()
    stack = list()
    order = list()

    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            stack.extend(reversed(graph[node]))
    return order


n, m, v = map(int, sys.stdin.readline().strip().split())
graph = init_graph(m)

print(*dfs(graph, v))
print(*bfs(graph, v))
