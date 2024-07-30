from collections import deque
import sys
input = sys.stdin.readline


def bfs(now, goal):
    visited = set()
    queue = deque()

    queue.append([now, 0])

    while queue:
        number, depth = queue.popleft()
        if number == goal:
            return depth
        if number not in visited:
            visited.add(number)
            next_numbers = [number - 1, number + 1, number * 2]
            for next in next_numbers:
                if 0 <= next < 100001 and next not in visited:
                    queue.append([next, depth + 1])


if __name__ == "__main__":
    now, goal = map(int, input().strip().split())
    print(bfs(now, goal))