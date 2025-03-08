from deque import Deque

if __name__ == "__main__":
    deque = Deque()

    print("Deque가 비어있는가?", deque.is_empty())

    # 앞에서 추가
    deque.add_first(10)
    deque.add_first(20)
    deque.add_first(30)

    print("앞에서 3개 추가 후:", end=" ")
    deque.print_all()

    # 뒤에서 추가
    deque.add_last(40)
    deque.add_last(50)

    print("뒤에서 2개 추가 후:", end=" ")
    deque.print_all()

    # 앞에서 제거
    deque.remove_first()

    print("앞에서 1개 제거 후:", end=" ")
    deque.print_all()

    # 뒤에서 제거
    deque.remove_last()

    print("뒤에서 1개 제거 후:", end=" ")
    deque.print_all()

    print("Deque가 비어있는가?", deque.is_empty())
