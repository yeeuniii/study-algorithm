from collections import deque
import sys
input = sys.stdin.readline


def bfs(n, m, miro):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque()
    queue.append(((1, 1), 1))

    while queue:
        (x, y), depth = queue.popleft()
        if (x, y) == (m, n):
            return depth
        for dx, dy in d:
            if 0 < x + dx <= m and 0 < y + dy <= n \
                    and miro[y + dy][x + dx] == '1':
                miro[y + dy][x + dx] = '0'
                queue.append([(x + dx, y + dy), depth + 1])


def main():
    n, m = map(int, input().strip().split())
    miro = list([0] for _ in range(n + 1))
    for idx in range(n):
        miro[idx + 1].extend(list(input().strip()))

    print(bfs(n, m, miro))


if __name__ == "__main__":
    main()