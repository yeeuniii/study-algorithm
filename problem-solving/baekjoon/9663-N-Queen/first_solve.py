import sys


def is_available(row, col, board):
    for idx in range(row):
        board_row = idx
        board_col = board[idx]
        if board_col == col:
            return False
        dx = row - board_row
        dy = col - board_col
        if dx == dy or dx == -dy:
            return False
    return True


def n_queen(n, row, board):
    if row == n:
        return 1

    cnt = 0
    for col in range(n):
        if is_available(row, col, board):
            board[row] = col
            cnt += n_queen(n, row + 1, board)
    return cnt


def main():
    n = int(sys.stdin.readline().strip())
    board = [0] * n
    print(n_queen(n, 0, board))


if __name__ == "__main__":
    main()