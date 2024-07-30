import sys
from collections import deque


def bfs(n, des):
    minimum_time = -1
    cnt = 0
    depths = [-1] * 100001
    queue = deque()

    queue.append(n)
    depths[n] = 0
    while queue:
        node = queue.popleft()
        depth = depths[node]
        if 0 <= minimum_time < depth:
            return minimum_time, cnt
        if node == des:
            if minimum_time == -1:
                minimum_time = depth
            cnt += 1

        for next in [node - 1, node + 1, node * 2]:
            if 0 <= next <= 100000 and (depths[next] == -1 or depths[next] == depth + 1):
                queue.append(next)
                depths[next] = depth + 1
    return minimum_time, cnt


def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    if n >= k:
        print(n - k, "\n", 1, sep="")
    else:
        minimum_time, cnt = bfs(n, k)
        print(minimum_time, "\n", cnt, sep="")


if __name__ == "__main__":
    main()
