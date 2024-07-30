import sys

n = int(sys.stdin.readline())
fibonacci_numbers = [1, 1]

for index in range(2, n):
    fibonacci_numbers.append(fibonacci_numbers[index - 1] + fibonacci_numbers[index - 2])

print(fibonacci_numbers[-1])