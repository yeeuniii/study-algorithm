from study.algorithm.binarysearch.binary_search import binary_search


def main():
    target = int(input())
    data = sorted(list(map(int, input().split())))

    print(binary_search(target, data))
    print(binary_search(max(data) + 1, data))


if __name__ == "__main__":
    main()