from collections import Counter

counter = Counter("hello world")
print(counter)

# 1. value update
print(counter['o'])
counter['o'] += 1
print(counter['o'])

counter['o'] = 0
print(counter['o'])

# 2. access
for key, value in counter.items():
    print(f"{key}: {value}")