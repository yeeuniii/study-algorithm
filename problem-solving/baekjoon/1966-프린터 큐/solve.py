from collections import deque
import sys


class Importance:
    def __init__(self, n, importance):
        self.importance = importance
        self.count = list(0 for _ in range(9))
        self.max = 0

        self.init_count()
        self.update_max_importance()

    def init_count(self):
        for i in self.importance:
            self.count[i - 1] += 1

    def update_max_importance(self):
        on_going = True

        while on_going and len(self.count) > 0:
            if self.count[-1] > 0:
                self.max = len(self.count)
                self.count[-1] -= 1
                on_going = False
            if self.count[-1] == 0:
                self.count.pop()


def find_print_order(n, m, importance):
    queue = deque(range(n))
    order = 0
    count = Importance(n, importance)

    while 1:
        num = queue.popleft()
        if importance[num] == count.max:
            count.update_max_importance()
            order += 1
            if num == m:
                break
        else:
            queue.append(num)
    return order


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    importance = list(map(int, sys.stdin.readline().strip().split()))
    print(find_print_order(n, m, importance))
