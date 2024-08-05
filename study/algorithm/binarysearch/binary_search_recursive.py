def recursive_binary_search(target, data, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    value = data[mid]
    if value == target:
        return mid

    if value > target:
        answer = recursive_binary_search(target, data, start, mid - 1)
    else:
        answer = recursive_binary_search(target, data, mid + 1, end)
    return answer