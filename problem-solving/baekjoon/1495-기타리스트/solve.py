import sys
input = lambda: sys.stdin.readline().strip()

n, start, maximum = map(int, input().split())
distances = list(map(int, input().split()))
volumes = [[False] * (maximum + 1) for _ in range(n)]


def update_volumes(idx, current, distance):
    if current - distance >= 0:
        volumes[idx][current- distance] = True
    if current + distance <= maximum:
        volumes[idx][current + distance] = True


def fill_volumes():
    update_volumes(0, start, distances[0])

    for idx in range(1, n):
        for volume in range(1, maximum + 1):
            if volumes[idx - 1][volume]:
                update_volumes(idx, volume, distances[idx])


def main():
    fill_volumes()

    last = volumes[-1]
    result = -1
    for idx, value in enumerate(last[::-1]):
        if value:
            result = maximum - idx
            break
    print(result)


if __name__ == "__main__":
    main()