import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    ps = sys.stdin.readline().strip()
    while "()" in ps:
        ps = ps.replace("()", "")
    if len(ps) == 0:
        print("YES")
    else:
        print("NO")