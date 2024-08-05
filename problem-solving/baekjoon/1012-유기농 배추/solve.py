import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)


def init_fields(width, height, k):
    fields = list([0] * width for _ in range(height))

    for _ in range(k):
        x, y = map(int, input().strip().split())
        fields[y][x] = 1
    return fields


def dfs(x, y, fields, width, height):
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    fields[y][x] = 0
    for dx, dy in d:
        if 0 <= x + dx < width and 0 <= y + dy < height \
                and fields[y + dy][x + dx] == 1:
            dfs(x + dx, y + dy, fields, width, height)
    return fields


def main():
    t = int(input().strip())

    for _ in range(t):
        width, height, k = map(int, input().strip().split())
        fields = init_fields(width, height, k)

        cnt = 0
        for x in range(width):
            for y in range(height):
                if fields[y][x] == 1:
                    fields = dfs(x, y, fields, width, height)
                    cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()