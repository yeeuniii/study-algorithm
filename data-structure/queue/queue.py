from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, element):
        self.queue.append(element)
        self.size += 1

    def dequeue(self):
        if not self.empty():
            self.queue.popleft()
            self.size -= 1

    def front(self):
        if not self.empty():
            return self.queue[0]
        return None

    def rear(self):
        if not self.empty():
            return self.queue[self.size - 1]
        return None

    def empty(self):
        return self.size == 0
