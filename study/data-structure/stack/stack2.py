import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "linkedlist")))

from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, data):
        self.stack.insert_at(0, data)

    def pop(self):
        try:
            return self.stack.delete_at(0)
        except AttributeError:
            return None

    def peek(self):
        return self.stack.get_node_at(0)

    def is_empty(self):
        return self.stack.count == 0
