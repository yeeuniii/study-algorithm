import sys
from collections import deque

v, e = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start_node):
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])


cnt = 0
visited = set()
for idx in range(v):
    if idx + 1 not in visited:
        bfs(idx + 1)
        cnt += 1

print(cnt)