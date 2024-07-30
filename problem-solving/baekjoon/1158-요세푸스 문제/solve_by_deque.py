from collections import deque
import sys

n, k = map(int, sys.stdin.readline().strip().split())
result = list()
empty_queue = deque()
filled_queue = deque()
for idx in range(n):
    filled_queue.append(idx + 1)

while len(result) < n:
    for idx in range(k - 1):
        if len(filled_queue) == 0:
            filled_queue = empty_queue
            empty_queue = deque()
        empty_queue.append(filled_queue.popleft())
    if len(filled_queue) == 0:
        filled_queue = empty_queue
        empty_queue = deque()
    result.append(filled_queue.popleft())

print("<", end="")
print(*result, sep=", ", end="")
print(">", end="")