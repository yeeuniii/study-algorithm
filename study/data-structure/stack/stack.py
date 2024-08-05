class Stack:
    def __init__(self):
        self.stack = list()
        self.size = 0

    def push(self, element):
        self.stack.append(element)
        self.size += 1

    def pop(self):
        if not self.empty():
            self.stack.pop()
            self.size -= 1

    def top(self):
        if not self.empty():
            return self.stack[self.size - 1]
        return None

    def empty(self):
        return self.size == 0
