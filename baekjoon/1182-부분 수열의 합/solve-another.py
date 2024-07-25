import sys
input = lambda: sys.stdin.readline().strip()


def backtracking(n, s, seq, total, idx):
    if idx == n:
        if total == s:
            return 1
        return 0

    cnt = backtracking(n, s, seq, total + seq[idx], idx + 1)
    cnt += backtracking(n, s, seq, total, idx + 1)
    return cnt


def main():
    n, s = map(int, input().split())
    seq = list(map(int, input().split()))
    result = backtracking(n, s, seq, 0, 0)
    if s == 0:
        result -= 1
    print(result)


if __name__ == "__main__":
    main()
