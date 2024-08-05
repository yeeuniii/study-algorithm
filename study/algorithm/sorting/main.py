import random
import time

from study.algorithm.sorting.quick import quick_sort
from study.algorithm.sorting.selection import selection_sort

data = list(range(int(input())))
random.shuffle(data)
print(f"origin: {data}\n")

# 삽입 정렬
print("삽입 정렬(Selection Sort)")
selection = data.copy()
start = time.time()
selection_sort(selection)
end = time.time()
print(f"sorted: {selection}")
print(f"time: {end - start:.6f} sec")

# 퀵 정렬
print("퀵 정렬(Quick Sort)")
quick = data.copy()
start = time.time()
quick_sort(quick, 0, len(data) - 1)
end = time.time()
print(f"sorted: {quick}")
print(f"time: {end - start:.6f} sec")
