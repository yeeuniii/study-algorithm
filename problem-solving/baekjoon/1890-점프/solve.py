import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]


def count():
    dp[0][0] = 1

    for y in range(n):
        for x in range(n):
            if x == y == n - 1:
                return dp[-1][-1]
            d = game[y][x]
            if x + d < n:
                dp[y][x + d] += dp[y][x]
            if y + d < n:
                dp[y + d][x] += dp[y][x]


if __name__ == "__main__":
    print(count())
