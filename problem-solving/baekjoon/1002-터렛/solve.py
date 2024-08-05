import sys
import math


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def solve(x1, y1, r1, x2, y2, r2):
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return -1
        return 0

    d = get_distance(x1, y1, x2, y2)
    if r1 < r2 + d and r2 < r1 + d and d < r1 + r2:
        return 2
    if r1 == r2 + d or r2 == r1 + d or d == r1 + r2:
        return 1
    return 0


def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        print(solve(*map(int, sys.stdin.readline().strip().split())))


if __name__ == "__main__":
    main()
