import sys
import math


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def solve(x1, y1, r1, x2, y2, r2):
    d = get_distance(x1, y1, x2, y2)

    if r1 == r2 and d == 0:
        return -1

    if abs(r1 - r2) < d < r1 + r2:
        return 2
    if d in [r1 + r2, abs(r1 - r2)]:
        return 1
    return 0


def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        print(solve(*map(int, sys.stdin.readline().strip().split())))


if __name__ == "__main__":
    main()
