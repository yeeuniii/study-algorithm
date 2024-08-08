import sys


def is_triangle(a, b, c):
    return c < a + b


a, b, c = sorted(map(int, sys.stdin.readline().strip().split()))
while (a, b, c) != (0, 0, 0):
    if not is_triangle(a, b, c):
        print("Invalid")
    else:
        s = {a, b, c}
        if len(s) == 1:
            print("Equilateral")
        elif len(s) == 2:
            print("Isosceles")
        else:
            print("Scalene")
    a, b, c = sorted(map(int, sys.stdin.readline().strip().split()))
