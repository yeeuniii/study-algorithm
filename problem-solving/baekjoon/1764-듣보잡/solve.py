import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
no_listen = set()
no_see = set()

for _ in range(n):
    no_listen.add(input())
for _ in range(m):
    no_see.add(input())

no_both = no_listen & no_see

print(len(no_both))
for no in sorted(no_both):
    print(no)
