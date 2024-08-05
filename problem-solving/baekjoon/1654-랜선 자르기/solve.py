import sys

input = lambda: sys.stdin.readline().strip()


def get_maximum_cable_length(n, cables):
    start = 1
    end = max(cables)
    answer = start

    while start <= end:
        mid = (start + end) // 2
        result = 0
        for cable in cables:
            result += cable // mid

        if result >= n:
            answer = mid
            start = mid + 1
        else:
            end = mid -1
    return answer


def main():
    k, n = map(int, input().split())
    cables = list()
    for _ in range(k):
        cables.append(int(input()))
    print(get_maximum_cable_length(n, cables))


if __name__ == "__main__":
    main()