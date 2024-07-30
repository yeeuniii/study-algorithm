import sys

input = lambda: sys.stdin.readline().strip()

from_alphabet = dict()
alphabets = "abcdefghijklmnopqrstuvwxyz"
for idx, alphabet in enumerate(alphabets):
    from_alphabet[alphabet] = idx + 1
for idx, alphabet in enumerate(alphabets):
    from_alphabet[alphabet.upper()] = idx + 27

word = input()
mappings = map(lambda idx: from_alphabet[idx], word)
number = sum(mappings)


def is_prime(number):
    if number == 1:
        return True

    prime = 2
    while prime * prime <= number:
        if number % prime == 0:
            return False
        prime += 1
    return True


if is_prime(number):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
