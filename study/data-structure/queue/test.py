from queue2 import Queue

if __name__ == "__main__":
    queue = Queue()

    print("큐가 비어 있는가?", queue.is_empty())  # True 예상

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("현재 front:", queue.front().data)  # 10 예상
    print("큐가 비어 있는가?", queue.is_empty())  # False 예상

    print("dequeue 실행:", queue.dequeue().data)  # 10 예상
    print("dequeue 실행:", queue.dequeue().data)  # 20 예상
    print("현재 front:", queue.front().data)  # 30 예상

    print("dequeue 실행:", queue.dequeue().data)  # 30 예상
    print("큐가 비어 있는가?", queue.is_empty())  # True 예상

    print("dequeue 실행 (비어있는 상태):", queue.dequeue())  # None 예상
    print("front 실행 (비어있는 상태):", queue.front())  # None 예상
