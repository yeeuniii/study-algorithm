import sys
input = lambda: sys.stdin.readline().strip()


def backtracking(n, s, seq, total, start_idx):
    if start_idx == n:
        return 0

    cnt = 0
    for idx in range(start_idx, n):
        if total + seq[idx] == s:
            cnt += 1
        cnt += backtracking(n, s, seq, total + seq[idx], idx + 1)
    return cnt


def main():
    n, s = map(int, input().split())
    seq = list(map(int, input().split()))
    print(backtracking(n, s, seq, 0, 0))


if __name__ == "__main__":
    main()
