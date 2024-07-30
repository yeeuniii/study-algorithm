import sys

input = lambda: sys.stdin.readline().strip()

VOWEL = {'a', 'e', 'i', 'o', 'u'}


def is_possible(l, number_of_vowel):
    return number_of_vowel >= 1 and l - number_of_vowel >= 2


def backtracking(l, c, chars, start, password, number_of_vowel):
    if len(password) == l and is_possible(l, number_of_vowel):
        return password + "\n"

    result = ""
    for idx in range(start, c):
        if chars[idx] in VOWEL:
            result += backtracking(l, c, chars, idx + 1, password + chars[idx], number_of_vowel + 1)
        else:
            result += backtracking(l, c, chars, idx + 1, password + chars[idx], number_of_vowel)
    return result


def main():
    l, c = map(int, input().split())
    chars = sorted(list(input().split()))
    print(backtracking(l, c, chars, 0, "", 0))


if __name__ == "__main__":
    main()
