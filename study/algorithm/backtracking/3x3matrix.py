import sys


def backtracking(matrix, row, score, visited_col):
    if row == 3:
        return score

    min_score = sys.maxsize

    for col in range(len(visited_col)):
        if not visited_col[col]:
            visited_col[col] = True
            current_score = backtracking(matrix, row + 1, score + matrix[row][col], visited_col)
            min_score = min(min_score, current_score)
            visited_col[col] = False
    return min_score


def main():
    matrix = [
        [1, 5, 3],
        [2, 4, 7],
        [5, 3, 5]
    ]
    visited_col = [False] * len(matrix[0])
    print(backtracking(matrix, 0, 0, visited_col))


if __name__ == "__main__":
    main()