import sys


class Stack:
    def __init__(self):
        self.stack = list()
        self.size = 0

    def push(self, element):
        self.stack.append(element)
        self.size += 1

    def pop(self):
        num = -1
        if not self.empty():
            num = self.stack.pop()
            self.size -= 1
        print(num)


    def size(self):
        print(self.size)


    def empty(self):
        is_empty = True
        if self.size > 0:
            is_empty = False
        print(int(is_empty))
        return is_empty

    def top(self):
        num = -1
        if not self.empty():
            num = self.stack[self.size - 1]
        print(num)


n = int(sys.stdin.readline())

