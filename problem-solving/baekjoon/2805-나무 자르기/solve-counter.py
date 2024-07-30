import sys
from collections import Counter

input = lambda: sys.stdin.readline().strip()


def get_maximum_height(wanted, heights):
    start = 1
    end = max(heights) - 1
    result = 0

    while start <= end:
        mid = (start + end) // 2

        tree = sum([(height - mid) * number if height > mid else 0 for height, number in heights.items()])
        if tree >= wanted:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result


def main():
    n, wanted = map(int, input().split())
    heights = Counter(list(map(int, input().split())))
    print(get_maximum_height(wanted, heights))


if __name__ == "__main__":
    main()
