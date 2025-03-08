import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from linkedlist.doubly_linked_list import DoublyLinkedList


class HashData:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self):
        self.array = [DoublyLinkedList() for _ in range(10)]

    @staticmethod
    def hash(key):
        return key % 10

    def set(self, key, value):
        self.array[self.hash(key)].insert_at(0, HashData(key, value))

    def get(self, key):
        values = self.array[self.hash(key)]
        node = values.head

        while node and node.data.key != key:
            node = node.next
        if node:
            return node.data.value
        return None

    def remove(self, key):
        values = self.array[self.hash(key)]
        node = values.head
        index = 0

        while node and node.data.key != key:
            node = node.next
            index += 1
        if node:
            values.delete_at(index)
        return None
