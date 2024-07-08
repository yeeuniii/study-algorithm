from stack import Stack

stack = Stack()
stack.push(1)
stack.push(10)
stack.push(100)

print("stack", stack.stack)
print("size is", stack.size)
print("top is", stack.top())

stack.pop()

print("\nAfter pop")
print("stack", stack.stack)
print("size is", stack.size)
print("top is", stack.top())
