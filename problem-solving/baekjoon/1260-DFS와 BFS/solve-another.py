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


def dfs(graph, node, visited):
    if not node or node in visited:
        return

    visited.append(node)
    for next in graph[node]:
        dfs(graph, next, visited)


def bfs(graph, start_node):
    queue = deque()
    queue.append(start_node)
    visited = list()

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


n, m, v = map(int, sys.stdin.readline().strip().split())
graph = init_graph(m)


visited = list()
dfs(graph, v, visited)
print(*visited)

print(*bfs(graph, v))
