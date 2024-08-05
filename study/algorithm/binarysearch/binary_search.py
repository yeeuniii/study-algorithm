def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if target == data[mid]:
            return mid

        if target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None
