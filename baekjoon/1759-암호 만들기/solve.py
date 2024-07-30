import sys

input = lambda: sys.stdin.readline().strip()

VOWEL = {'a', 'e', 'i', 'o', 'u'}


def is_possible(l, number_of_vowel):
    return number_of_vowel >= 1 and l - number_of_vowel >= 2


def backtracking(l, c, chars, password, index, current, number_of_vowel):
    if index == l and is_possible(l, number_of_vowel):
        return password + "\n"
    if current == c:
        return ""

    if chars[current] in VOWEL:
        result = backtracking(l, c, chars, password + chars[current], index + 1, current + 1, number_of_vowel + 1)
    else:
        result = backtracking(l, c, chars, password + chars[current], index + 1, current + 1, number_of_vowel)
    result += backtracking(l, c, chars, password, index, current + 1, number_of_vowel)
    return result


def main():
    l, c = map(int, input().split())
    chars = sorted(list(input().split()))
    print(backtracking(l, c, chars, "", 0, 0, 0))


if __name__ == "__main__":
    main()
