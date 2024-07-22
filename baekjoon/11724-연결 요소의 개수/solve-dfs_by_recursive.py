import sys
sys.setrecursionlimit(10**6)

v, e = map(int, sys.stdin.readline().strip().split())
graph = list([False] * (v + 1) for _ in range(v + 1))

for _ in range(e):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = True
    graph[b][a] = True


def dfs(node):
    if node in visited:
        return 0
    visited.add(node)
    for idx in range(v):
        if idx + 1 not in visited and graph[node][idx + 1]:
            dfs(idx + 1)
    return 1


cnt = 0
visited = set()
for idx in range(v):
    cnt += dfs(idx + 1)

print(cnt)