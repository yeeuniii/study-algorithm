import sys


def n_queen(n, row, visited_columns, visited_increase, visited_decrease):
    if row == n:
        return 1

    cnt = 0
    for col in range(n):
        if not visited_columns[col] and not visited_increase[row + col] and not visited_decrease[col - row + n]:
            visited_columns[col] = visited_increase[row + col] = visited_decrease[col - row + n] = True
            cnt += n_queen(n, row + 1, visited_columns, visited_increase, visited_decrease)
            visited_columns[col] = visited_increase[row + col] = visited_decrease[col - row + n] = False
    return cnt


def main():
    n = int(sys.stdin.readline().strip())
    visited_columns = [False] * n
    visited_increase = [False] * (2 * n - 1)
    visited_decrease = [False] * (2 * n)
    print(n_queen(n, 0, visited_columns, visited_increase, visited_decrease))


if __name__ == "__main__":
    main()
