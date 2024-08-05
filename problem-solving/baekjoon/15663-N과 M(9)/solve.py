import sys

input = lambda: sys.stdin.readline().strip()


def backtracking(m, numbers, index, visited, seq, duplicated):
    if index == m:
        if tuple(seq) not in duplicated:
            print(*seq)
            duplicated.add(tuple(seq))
        return

    for numbers_index, number in enumerate(numbers):
        if numbers_index not in visited:
            seq.append(number)
            visited.add(numbers_index)
            backtracking(m, numbers, index + 1, visited, seq, duplicated)
            visited.remove(numbers_index)
            seq.pop()


def main():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    backtracking(m, numbers, 0, set(), list(), set())


if __name__ == "__main__":
    main()