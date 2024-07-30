import sys

CARDINAL_POINTS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0


def get_simple_path_prob(n, probs, visited, depth, prob, x, y):
    if depth == n:
        global result
        result += prob
        return

    visited[y][x] = True
    for idx in range(4):
        dx, dy = CARDINAL_POINTS[idx]
        nex_x, nex_y = x + dx, y + dy
        if not visited[nex_y][nex_x]:
            get_simple_path_prob(n, probs, visited, depth + 1, prob * probs[idx], nex_x, nex_y)
    visited[y][x] = False


def main():
    probs = list(map(int, sys.stdin.readline().strip().split()))
    n = probs.pop(0)
    probs = list(map(lambda prob: prob/100, probs))
    visited = list([False] * (2 * n + 1) for _ in range(2 * n + 1))

    get_simple_path_prob(n, probs, visited, 0, 1, 0, 0)
    print(result)


if __name__ == "__main__":
    main()
