class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def has_next(self):
        return self.next