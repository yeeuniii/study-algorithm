import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())
# words = defaultdict(set)
#
# for _ in range(n):
#     word = sys.stdin.readline().strip()
#     words[len(word)].add(word)
#
# for key in sorted(words.keys()):
#     for word in sorted(words[key]):
#         print(word)
#     # print("\n".join(sorted(words[key])))
#
#

words = list(list() for _ in range(51))

for _ in range(n):
    word = sys.stdin.readline().strip()
    words[len(word)].append(word)

for idx in range(50):
    if words[idx + 1]:
        print("\n".join(sorted(set(words[idx + 1]))))