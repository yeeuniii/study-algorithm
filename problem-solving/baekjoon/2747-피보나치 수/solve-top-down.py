import sys

n = int(sys.stdin.readline())
fibonacci_numbers = [1, 1]


def fibonacci(index):
    if index == 0 or index == 1:
        return 1
    if index < len(fibonacci_numbers):
        return fibonacci_numbers[index]
    fibonacci_numbers.append(fibonacci(index - 1) + fibonacci(index - 2))
    return fibonacci_numbers[-1]


print(fibonacci(n - 1))