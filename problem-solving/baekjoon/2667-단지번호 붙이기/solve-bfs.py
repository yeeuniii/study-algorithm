import sys
from collections import deque

n = int(sys.stdin.readline().strip())
graph = list(list(sys.stdin.readline().strip()) for _ in range(n))

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(start_x, start_y):
    cnt = 0
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()
        if graph[y][x] == '1':
            graph[y][x] = '0'
            cnt += 1
            for dx, dy in d:
                if 0 <= x + dx < n and 0 <= y + dy < n \
                        and graph[y + dy][x + dx]:
                    queue.append((x + dx, y + dy))
    return cnt


result = list()
for x in range(n):
    for y in range(n):
        if cnt := bfs(x, y):
            result.append(cnt)

print(len(result))
result.sort()
for num in result:
    print(num)