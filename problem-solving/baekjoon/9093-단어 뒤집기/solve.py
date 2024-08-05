import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    strings = list(sys.stdin.readline().strip().split())
    for string in strings:
        print(string[::-1] + " ", end="")
