from stack2 import Stack

if __name__ == "__main__":
    stack = Stack()

    print("스택이 비어 있는가?", stack.is_empty())  # True 예상

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("현재 스택 top:", stack.peek().data)  # 30 예상
    print("스택이 비어 있는가?", stack.is_empty())  # False 예상

    print("pop 실행:", stack.pop().data)  # 30 예상
    print("pop 실행:", stack.pop().data)  # 20 예상
    print("현재 스택 top:", stack.peek().data)  # 10 예상

    print("pop 실행:", stack.pop().data)  # 10 예상
    print("스택이 비어 있는가?", stack.is_empty())  # True 예상
