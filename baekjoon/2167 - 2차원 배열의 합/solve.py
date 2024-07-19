import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = list([0] for _ in range(n + 1))
for idx in range(n):
    arr[idx + 1].extend(map(int, input().strip().split()))


def sum_array(i, j, x, y):
    total = 0

    for v in range(i, x + 1):
        total += sum(arr[v][j:y+1])
    return total


k = int(input().strip())
for _ in range(k):
    i, j, x, y = map(int, input().strip().split())
    print(sum_array(i, j, x, y))
