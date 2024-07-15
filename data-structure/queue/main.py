from queue import Queue

qu = Queue()

qu.enqueue(-1)
qu.enqueue(0)
qu.enqueue(1)
qu.enqueue(2)

print("Queue :", qu.queue)
print("size :", qu.size)
print("front :", qu.front())
print("rear :", qu.rear())

qu.dequeue()

print("\nAfter dequeue")
print("Queue :", qu.queue)
print("size :", qu.size)
print("front :", qu.front())
print("rear :", qu.rear())
