import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from hashtable.hash_table import HashTable


class Set:
    def __init__(self):
        self.set = HashTable()

    def add(self, data):
        if self.set.get(data) is None:
            self.set.set(data, 0)

    def is_contain(self, data):
        return self.set.get(data) is not None

    def remove(self, data):
        self.set.remove(data)

    def clear(self):
        for lst in self.set.array:
            lst.clear()

    def is_empty(self):
        for lst in self.set.array:
            if lst.count > 0:
                return False
        return True

    def print_all(self):
        for lst in self.set.array:
            node = lst.head
            while node:
                print(node.data.key, end=" ")
                node = node.next
        print()
