import sys
sys.setrecursionlimit(10**5)


def is_good_sequence(sequence):
    n = len(sequence)

    for size in range(1, int(n / 2) + 1):
        if sequence[-size:] == sequence[-size*2:-size]:
            return False
    return True


def backtracking(n, index, seq):
    if index == n:
        print(seq)
        return True

    for num in "123":
        if is_good_sequence(seq + num):
            if backtracking(n, index + 1, seq + num):
                return True
    return False


def main():
    n = int(sys.stdin.readline().strip())
    backtracking(n, 0, "")


if __name__ == "__main__":
    main()
