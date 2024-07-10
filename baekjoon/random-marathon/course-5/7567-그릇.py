import sys

plates = sys.stdin.readline().strip()
height = 10

for idx in range(len(plates) - 1):
    increase = 10
    if plates[idx] == plates[idx + 1]:
        increase = 5
    height += increase

print(height)
