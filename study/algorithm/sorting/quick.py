import sys

sys.setrecursionlimit(10**5)


def quick_sort(data):
    if len(data) < 2:
        return data

    pivot = data.pop()
    less = list()
    greater = list()

    for num in data:
        if num <= pivot:
            less.append(num)
        else:
            greater.append(num)
    return quick_sort(less) + [pivot] + quick_sort(greater)
