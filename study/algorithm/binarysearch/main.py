from study.algorithm.binarysearch.binary_search import binary_search
from study.algorithm.binarysearch.binary_search_recursive import recursive_binary_search


def main():
    target = int(input())
    data = sorted(list(map(int, input().split())))

    print(binary_search(target, data))
    print(binary_search(max(data) + 1, data))

    print(recursive_binary_search(target, data, 0, len(data) - 1))
    print(recursive_binary_search(max(data) + 1, data, 0, len(data) - 1))


if __name__ == "__main__":
    main()