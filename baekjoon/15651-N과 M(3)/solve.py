import sys

input = lambda: sys.stdin.readline().strip()


def backtracking(n, m, index, seq):
    if index == m:
        print(*seq)
        return

    for number in range(1, n + 1):
        seq[index] = number
        backtracking(n, m, index + 1, seq)


def main():
    n, m = map(int, input().split())
    backtracking(n, m, 0, [0] * m)


if __name__ == "__main__":
    main()