import sys


class Stack:
    def __init__(self):
        self.stack = list()
        self.ssize = 0

    def push(self, element):
        self.stack.append(element)
        self.ssize += 1

    def pop(self):
        num = -1
        if self.ssize > 0:
            num = self.stack.pop()
            self.ssize -= 1
        print(num)

    def size(self):
        print(self.ssize)

    def empty(self):
        is_empty = True
        if self.ssize > 0:
            is_empty = False
        print(int(is_empty))

    def top(self):
        num = -1
        if self.ssize > 0:
            num = self.stack[self.ssize - 1]
        print(num)


n = int(sys.stdin.readline())
cmds = list(sys.stdin.readline().strip().split() for _ in range(n))

stack = Stack()
funcs = {
    "pop": stack.pop,
    "size": stack.size,
    "empty": stack.empty,
    "top": stack.top
}

for idx in range(n):
    cmd = cmds[idx][0]
    if cmd == "push":
        num = int(cmds[idx][1])
        stack.push(num)
    else:
        funcs[cmd]()
