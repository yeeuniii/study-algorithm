import sys

v, e = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start_node, visited):
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(reversed(graph[node]))
    return visited


cnt = 0
visited = set()
for idx in range(v):
    if idx + 1 not in visited:
        visited = dfs(idx + 1, visited)
        cnt += 1

print(cnt)