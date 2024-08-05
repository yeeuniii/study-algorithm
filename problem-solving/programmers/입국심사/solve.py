def solution(n, times):
    first = 1
    last = max(times) * n

    while first <= last:
        mid = (first + last) // 2
        possible = 0
        for time in times:
            possible += mid // time

        if possible >= n:
            last = mid - 1
        else:
            first = mid + 1

    return first


print(solution(6, [7, 10]))
print()
print(solution(7, [1, 2, 3]))