import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from linkedlist.doubly_linked_list import DoublyLinkedList

class Deque:
    def __init__(self):
        self.deque = DoublyLinkedList()

    def print_all(self):
        self.deque.print_all()

    def add_first(self, data):
        self.deque.insert_at(0, data)

    def remove_first(self):
        self.deque.delete_at(0)

    def add_last(self, data):
        self.deque.insert_last(data)

    def remove_last(self):
        self.deque.delete_last()

    def is_empty(self):
        return self.deque.count == 0
