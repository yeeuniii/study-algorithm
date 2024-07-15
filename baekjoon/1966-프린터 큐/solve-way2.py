import sys


def solve(n, m, importance):
    cnt = 1

    while 1:
        if importance[0] < max(importance):
            importance.append(importance.pop(0))
        else:
            if m == 0:
                return cnt
            else:
                importance.pop(0)
                cnt += 1

        m -= 1
        if m < 0:
            m = len(importance) - 1


def main():
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().strip().split())
        importance = list(map(int, sys.stdin.readline().strip().split()))
        print(solve(n, m, importance))


if __name__ == "__main__":
    main()
