import sys
from collections import deque

v, e = map(int, sys.stdin.readline().strip().split())
graph = [[False] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = True
    graph[b][a] = True


def bfs(start_node):
    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for idx in range(v):
                if graph[node][idx + 1]:
                    queue.append(idx + 1)


cnt = 0
visited = set()
for idx in range(v):
    if idx + 1 not in visited:
        bfs(idx + 1)
        cnt += 1

print(cnt)