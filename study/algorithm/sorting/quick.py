import sys
sys.setrecursionlimit(10**5)


def swap(data, left, right):
    data[left], data[right] = data[right], data[left]


def partition(data, left, right):
    pivot = data[left]
    less = left
    greater = right

    while less < greater:
        while less < greater and data[greater] > pivot:
            greater -= 1
        while less < greater and data[less] <= pivot:
            less += 1
        swap(data, less, greater)
    swap(data, left, less)
    return less


def quick_sort(data, left, right):
    if left < right:
        pivot = partition(data, left, right)
        quick_sort(data, left, pivot - 1)
        quick_sort(data, pivot + 1, right)
    return data
