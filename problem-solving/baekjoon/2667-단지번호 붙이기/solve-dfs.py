import sys


n = int(sys.stdin.readline().strip())
graph = list(list(sys.stdin.readline().strip()) for _ in range(n))

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_invalid(x):
    return x < 0 or x >= n


def dfs(x, y):
    if is_invalid(x) or is_invalid(y):
        return False

    if graph[y][x] == '1':
        graph[y][x] = '0'
        global cnt
        cnt += 1
        for dx, dy in d:
            dfs(x + dx, y + dy)
        return True
    return False


cnt = 0
result = list()

for x in range(n):
    for y in range(n):
        if dfs(x, y):
            result.append(cnt)
            cnt = 0

print(len(result))
result.sort()
for cnt in result:
    print(cnt)