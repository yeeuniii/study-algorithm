import sys

RIGHT = '('
LEFT = ')'


def is_vps(ps):
    cnt = 0

    if ps[0] == LEFT:
        return "NO"
    for char in ps:
        if char == RIGHT:
            cnt += 1
        elif cnt > 0:
            cnt -= 1
        else:
            return "NO"
    if cnt > 0:
        return "NO"
    return "YES"


def main():
    t = int(sys.stdin.readline().strip())
    pss = list(sys.stdin.readline().strip() for _ in range(t))

    for ps in pss:
        print(is_vps(ps))


if __name__ == '__main__':
    main()
