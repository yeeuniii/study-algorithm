from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def print_all(self):
        node = self.head

        while node:
            print(node.data, end=" ➡ ")
            node = node.next
        print("None")

    def clear(self):
        self.head = None
        self.count = 0

    def insert_at(self, index, data):
        if index < 0 or index > self.count:
            raise IndexError("IndexError: Out of Range")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.count += 1
            return

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        new_node.next = prev.next
        prev.next = new_node
        self.count += 1

    def insert_last(self, data):
        self.insert_at(self.count, data)

    def delete_at(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("IndexError: Out of Range")

        if self.head is None:
            raise AttributeError("AttributeError: head is None")

        if index == 0:
            delete_node = self.head
            self.head = self.head.next
            self.count -= 1
            return delete_node

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        delete_node = prev.next
        prev.next = prev.next.next
        self.count -= 1
        return delete_node

    def delete_last(self):
        self.delete_at(self.count - 1)

    def get_node_at(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("IndexError: Out of Range")

        node = self.head

        for _ in range(index):
            node = node.next
        return node
