import sys

xs = set()
ys = set()
for _ in range(3):
    x, y = sys.stdin.readline().strip().split()
    if x in xs:
        xs.remove(x)
    else:
        xs.add(x)
    if y in ys:
        ys.remove(y)
    else:
        ys.add(y)

print(*xs, *ys)
