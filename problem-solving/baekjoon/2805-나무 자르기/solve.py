import sys

input = lambda: sys.stdin.readline().strip()


def get_maximum_height(wanted, heights):
    start = 0
    end = max(heights) - 1

    while start <= end:
        mid = (start + end) // 2

        trees = map(lambda h: h - mid if h > mid else 0, heights)
        if sum(trees) >= wanted:
            start = mid + 1
        else:
            end = mid - 1
    return end


def main():
    n, wanted = map(int, input().split())
    heights = list(map(int, input().split()))
    print(get_maximum_height(wanted, heights))


if __name__ == "__main__":
    main()
