import sys

input = sys.stdin.readline


def init_fields():
    for _ in range(number):
        x, y = map(int, input().strip().split())
        fields[y][x] = 1


def bfs(start_x, start_y):
    queue = [(start_x, start_y)]

    while queue:
        x, y = queue.pop(0)
        for dx, dy in d:
            if 0 <= x + dx < width and 0 <= y + dy < height \
                    and fields[y + dy][x + dx] == 1:
                fields[y + dy][x + dx] = 0
                queue.append((x + dx, y + dy))


d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

t = int(input().strip())

for _ in range(t):
    width, height, number = map(int, input().strip().split())
    fields = list([0] * width for _ in range(height))
    init_fields()

    cnt = 0
    for x in range(width):
        for y in range(height):
            if fields[y][x] == 1:
                bfs(x, y)
                cnt += 1
    print(cnt)