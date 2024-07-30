import sys

t = int(sys.stdin.readline().strip())
strings = list(sys.stdin.readline().strip() for _ in range(t))

for idx in range(t):
    string = strings[idx]
    last_idx = len(string) - 1
    print(string[0] + string[last_idx])
