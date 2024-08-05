import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    strings = list(sys.stdin.readline().strip().split())
    reversed_string = " ".join(string[::-1] for string in strings)
    print(reversed_string)