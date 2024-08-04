import sys
input = lambda: sys.stdin.readline().strip()


class Stack:
    def __init__(self):
        self.size = 0
        self.stack = list()

    def push(self, x):
        self.stack.append(x)
        self.size += 1

    def pop(self):
        if self.size:
            self.size -= 1
            print(self.stack.pop())
        else:
            print(-1)

    def get_size(self):
        print(self.size)

    def empty(self):
        print(0 if self.size > 0 else 1)

    def print_top(self):
        if self.size:
            print(self.stack[-1])
        else:
            print(-1)


def main():
    n = int(input())
    commands = [list(map(int, input().split())) for _ in range(n)]
    stack = Stack()
    methods = [stack.pop, stack.get_size, stack.empty, stack.print_top]

    for command in commands:
        number = command[0]
        if number == 1:
            stack.push(command[1])
        else:
            methods[number - 2]()


if __name__ == "__main__":
    main()
