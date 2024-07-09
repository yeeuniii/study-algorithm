import sys

n, k = map(int, sys.stdin.readline().strip().split())
lst = list(range(1, n + 1))
result = list()
idx = 0

for _ in range(n):
    idx += k - 1
    if idx >= len(lst):
        idx %= len(lst)
    result.append(lst.pop(idx))

print("<", end="")
print(*result, sep=", ", end="")
print(">", end="")
