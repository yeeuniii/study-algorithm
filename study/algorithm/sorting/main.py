import random
import time

from study.algorithm.sorting.quick import quick_sort
from study.algorithm.sorting.selection import selection_sort

data = list(range(1000))
random.shuffle(data)
print(f"origin: {data}\n")


def sort(sorting, method, data):
    print(f"# {sorting}")
    start = time.time()
    sorted_data = method(data)
    end = time.time()
    print(f"sorted: {sorted_data}")
    print(f"time: {end - start:.6f} sec")
    print()


sort("삽입 정렬(Selection Sort)", selection_sort, data.copy())
sort("퀵 정렬(Quick Sort)", quick_sort, data.copy())
