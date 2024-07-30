import sys
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().strip()

n, m, k = map(int, input().split())
trash = list([False] * (m + 1) for _ in range(n + 1))
for _ in range(k):
    r, c = map(int, input().split())
    trash[r][c] = True

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x, y):
    if not trash[y][x]:
        return 0

    cnt = 1
    trash[y][x] = False
    for dx, dy in d:
        if 0 < x + dx <= m and 0 < y + dy <= n \
                and trash[y + dy][x + dx]:
            cnt += dfs(x + dx, y + dy)
    return cnt


counts = list()
for x in range(m):
    for y in range(n):
        if trash[y + 1][x + 1]:
            counts.append(dfs(x + 1, y + 1))

print(max(counts))
