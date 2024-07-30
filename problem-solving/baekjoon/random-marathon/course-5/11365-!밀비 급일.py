import sys

while (password := sys.stdin.readline().strip()) != "END":
    size = len(password)
    for idx in range(1, size + 1):
        print(password[idx * -1], end="")
    print()
