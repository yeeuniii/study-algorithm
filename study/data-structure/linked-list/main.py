from Node import Node

head = Node(1)
head.next = Node(10)
head.next.next = Node(100)

node = head
while node:
    print(node.data)
    node = node.next
