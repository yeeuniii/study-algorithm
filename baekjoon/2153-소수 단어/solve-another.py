import sys

input = lambda: sys.stdin.readline().strip()

from_alphabet = dict()
num = ord('a')
while num <= ord('z'):
    from_alphabet[chr(num)] = num - ord('a') + 1
    num += 1
num = ord('A')
while num <= ord('Z'):
    from_alphabet[chr(num)] = num - ord('A') + 27
    num += 1

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
