import sys

input = lambda: sys.stdin.readline().strip()

n, budget, hotel, weeks = map(int, input().split())


minimum = 500001
for _ in range(hotel):
    hotel_price = int(input())
    possible_people = list(map(int, input().split()))
    if n * hotel_price > budget:
        continue
    for people in possible_people:
        if people >= n:
            minimum = min(n * hotel_price, minimum)
            continue

if minimum == 500001:
    print("stay home")
else:
    print(minimum)