from collections import deque
import sys


# deque
def find_print_order_using_deque(n, m, importance):
    printer = deque(range(n))
    sorted_importance = sorted(importance)
    idx = -1
    cnt = 0

    while idx != m:
        doc = printer.popleft()
        max = sorted_importance[-1]
        if importance[doc] == max:
            cnt += 1
            idx = doc
            sorted_importance.pop()
        else:
            printer.append(doc)
    return cnt


# list
def find_print_order_using_list(n, m, importance):
    printer = list(range(n))
    sorted_importance = sorted(importance)
    idx = -1
    cnt = 0

    while idx != m:
        doc = printer.pop(0)
        max = sorted_importance[-1]
        if importance[doc] == max:
            cnt += 1
            idx = doc
            sorted_importance.pop()
        else:
            printer.append(doc)
    return cnt


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    importance = list(map(int, sys.stdin.readline().strip().split()))
    print(find_print_order_using_list(n, m, importance))