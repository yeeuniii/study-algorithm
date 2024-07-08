from collections import deque
import sys


class Queue:
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, element):
        self.queue.append(element)
        self.size += 1

    def dequeue(self):
        if not self.empty():
            self.size -= 1
            return self.queue.popleft()
        return None

    def empty(self):
        return self.size == 0


n, k = map(int, sys.stdin.readline().strip().split())
res = list()
empty_queue = Queue()
filled_queue = Queue()
for idx in range(n):
    filled_queue.enqueue(idx + 1)


while len(res) < n:
    for idx in range(k - 1):
        if filled_queue.empty():
            filled_queue = empty_queue
            empty_queue = Queue()
        empty_queue.enqueue(filled_queue.dequeue())
    if filled_queue.empty():
        filled_queue = empty_queue
        empty_queue = Queue()
    res.append(filled_queue.dequeue())

print("<", end="")
print(*res, sep=", ", end="")
print(">", end="")
