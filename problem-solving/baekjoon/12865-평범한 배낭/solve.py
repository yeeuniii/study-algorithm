import sys

input = lambda: sys.stdin.readline().strip()


WEIGHT = 0
VALUE = 1


def get_maximum_value(n, max_weight, items):
    grids = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for weight in range(items[0][WEIGHT], max_weight + 1):
        grids[1][weight] = items[0][VALUE]
    for item in range(1, n):
        item_weight = items[item][WEIGHT]
        item_value = items[item][VALUE]
        for idx in range(1, min(item_weight, max_weight + 1)):
            grids[item + 1][idx] = grids[item][idx]
        for weight in range(item_weight, max_weight + 1):
            grids[item + 1][weight] = max(grids[item][weight], item_value + grids[item][weight - item_weight])
    return grids[n][max_weight]


def main():
    n, max_weight = map(int, input().split())
    items = list()
    for _ in range(n):
        items.append(list(map(int, input().split())))
    print(get_maximum_value(n, max_weight, items))


if __name__ == "__main__":
    main()