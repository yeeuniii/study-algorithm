class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def connect(self, node):
        self.next = node
        if node:
            node.prev = self

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def print_all(self):
        node = self.head

        while node:
            print(node.data, end="➡")
            node = node.next
        print("None")

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_at(self, index, data):
        if index < 0 or index > self.count:
            raise IndexError("IndexError: Out of Range")

        new_node = Node(data)
        prev_node = self.head

        if self.count == 0:
            self.head = new_node
            self.tail = new_node
            self.count += 1
            return

        if index == 0:
            new_node.connect(self.head)
            self.head = new_node
            self.count += 1
            return

        if index == self.count:
            self.tail.connect(new_node)
            self.tail = new_node
            self.count += 1
            return

        for _ in range(index - 1):
            prev_node = prev_node.next

        new_node.connect(prev_node.next)
        prev_node.connect(new_node)
        self.count += 1

    def insert_last(self, data):
        self.insert_at(self.count, data)

    def delete_at(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("IndexError: Out of Range")

        if self.head is None:
            raise AttributeError("AttributeError: head is None")

        if self.count == 1:
            delete_node = self.head
            self.clear()
            return delete_node

        if index == 0:
            delete_node = self.head
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return delete_node

        if index == self.count - 1:
            delete_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1
            return delete_node

        prev = self.head
        for _ in range(index - 1):
            prev = prev.next

        delete_node = prev.next
        prev.connect(prev.next.next)
        self.count -= 1
        return delete_node

    def delete_last(self):
        return self.delete_at(self.count - 1)

    def get_node_at(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("IndexError: Out of Range")

        node = self.head
        for _ in range(index):
            node = node.next
        return node
