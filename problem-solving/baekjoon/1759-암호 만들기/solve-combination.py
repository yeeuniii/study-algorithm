import sys
from itertools import combinations

input = lambda: sys.stdin.readline().strip()

VOWEL = {'a', 'e', 'i', 'o', 'u'}


def is_valid(l, number_of_vowel):
    return number_of_vowel >= 1 and l - number_of_vowel >= 2


def check_password(password, l):
    number_of_vowel = 0
    for c in password:
        if c in VOWEL:
            number_of_vowel += 1
    return is_valid(l, number_of_vowel)


def main():
    l, c = map(int, input().split())
    chars = sorted(list(input().split()))
    all_password = combinations(chars, l)

    result = list()
    for password in all_password:
        if check_password(password, l):
            result.append("".join(password))
    print("\n".join(result))


if __name__ == "__main__":
    main()
