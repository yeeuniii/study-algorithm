import sys
from collections import deque


def bfs(n, des):
    minimum_time = -1
    cnt = 0
    visited = set()
    queue = deque()

    queue.append((n, 0))
    while queue:
        node, depth = queue.popleft()
        if node == des:
            if minimum_time == -1:
                minimum_time = depth
            elif depth > minimum_time:
                return minimum_time, cnt
            cnt += 1

        visited.add(node)
        next_nodes = [node - 1, node + 1, node * 2]
        for next in next_nodes:
            if 0 <= next <= 100000 and next not in visited:
                queue.append((next, depth + 1))
    # return minimum_time, cnt


def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    if n >= k:
        print(n - k, "\n", 1, sep="")
    else:
        minimum_time, cnt = bfs(n, k)
        print(minimum_time, "\n", cnt, sep="")


if __name__ == "__main__":
    main()
