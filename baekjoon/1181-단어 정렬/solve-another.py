import sys

n = int(sys.stdin.readline().strip())
words = list(list() for _ in range(51))

for _ in range(n):
    word = sys.stdin.readline().strip()
    words[len(word)].append(word)

for idx in range(50):
    if words[idx + 1]:
        print("\n".join(sorted(set(words[idx + 1]))))