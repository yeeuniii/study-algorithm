import sys

numbers = list(map(int, sys.stdin.readline().strip().split()))
result1 = numbers[0] * numbers[1] / numbers[2]
result2 = numbers[0] / numbers[1] * numbers[2]
result = result1 if result1 > result2 else result2
print(int(result))