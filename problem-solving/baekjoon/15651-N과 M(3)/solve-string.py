import sys

input = lambda: sys.stdin.readline().strip()


def backtracking(n, m, index, seq):
    if index == m:
        return " ".join(seq) + "\n"

    result = ""
    for number in range(1, n + 1):
        result += backtracking(n, m, index + 1, seq + str(number))
    return result


def main():
    n, m = map(int, input().split())
    print(backtracking(n, m, 0, ""))


if __name__ == "__main__":
    main()