import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from linkedlist.doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, data):
        self.queue.insert_last(data)

    def dequeue(self):
        try:
            return self.queue.delete_at(0)
        except IndexError:
            return None

    def front(self):
        try:
            return self.queue.get_node_at(0)
        except IndexError:
            return None

    def is_empty(self):
        return self.queue.count == 0
