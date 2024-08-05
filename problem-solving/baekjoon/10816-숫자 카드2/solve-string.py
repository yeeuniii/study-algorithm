import sys

input = lambda: sys.stdin.readline().strip()


def main():
    n = int(input())
    counts = dict()
    cards = input().split()
    for card in cards:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    m = int(input())
    keys = input().split()
    result = ""
    for key in keys:
        if key in counts:
            result += str(counts[key]) + " "
        else:
            result += "0 "
    print(result)


if __name__ == "__main__":
    main()