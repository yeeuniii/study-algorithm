import sys
from itertools import product

input = lambda: sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    numbers = [str(i) for i in range(1, n + 1)]
    seqs = map(" ".join, list(product(numbers, repeat=m)))
    print("\n".join(seqs))


if __name__ == "__main__":
    main()