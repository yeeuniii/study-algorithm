import sys

input = lambda: sys.stdin.readline().strip()


def backtracking(size, numbers, index, seq, visited):
    if index == size:
        print(*seq)
        return

    before = 0
    for idx, number in enumerate(numbers):
        if idx not in visited and number != before:
            visited.add(idx)
            seq.append(number)
            before = number
            backtracking(size, numbers, index + 1, seq, visited)
            seq.pop()
            visited.remove(idx)


def main():
    n, m = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))

    backtracking(m, numbers, 0, list(), set())


if __name__ == "__main__":
    main()