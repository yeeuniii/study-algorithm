import sys
input = lambda: sys.stdin.readline().strip()


def get_maximum_price(n, terms, prices):
    dp = [0] * (n + 1)

    for day in range(n - 1, -1, -1):
        dp[day] = dp[day + 1]
        if day + terms[day] <= n:
            dp[day] = max(dp[day + 1], dp[day + terms[day]] + prices[day])
    return dp[0]


def main():
    n = int(input())
    terms = list()
    prices = list()
    for _ in range(n):
        term, price = map(int, input().split())
        terms.append(term)
        prices.append(price)
    print(get_maximum_price(n, terms, prices))


if __name__ == "__main__":
    main()
