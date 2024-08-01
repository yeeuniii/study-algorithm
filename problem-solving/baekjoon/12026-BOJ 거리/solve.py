import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
boj = list(input())

inf = float('inf')
result = [inf] * (n + 1)
result[1] = 0

for start in range(1, n + 1):
    for end in range(start + 1, n + 1):
        for current, next in [('B', 'O'), ('O', 'J'), ('J', 'B')]:
            if boj[start - 1] == current and boj[end - 1] == next:
                result[end] = min(result[end], result[start] + (end - start) ** 2)

print(result[-1] if result[-1] != inf else -1)