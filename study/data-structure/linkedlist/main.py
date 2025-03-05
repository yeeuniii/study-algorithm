from linked_list import LinkedList

if __name__ == "__main__":
    ll = LinkedList()

    # Test: insert_last on empty list
    print("Insert last on empty list:")
    ll.insert_last(10)
    ll.print_all()  # Expected: 10 ➡ None

    # Test: insert_last on non-empty list
    print("Insert last on non-empty list:")
    ll.insert_last(20)
    ll.insert_last(30)
    ll.print_all()  # Expected: 10 ➡ 20 ➡ 30 ➡ None

    # Test: insert_at at index 1
    print("Insert at index 1 (value 15):")
    ll.insert_at(1, 15)
    ll.print_all()  # Expected: 10 ➡ 15 ➡ 20 ➡ 30 ➡ None

    # Test: insert_at at index 0 (head)
    print("Insert at index 0 (value 5):")
    ll.insert_at(0, 5)
    ll.print_all()  # Expected: 5 ➡ 10 ➡ 15 ➡ 20 ➡ 30 ➡ None

    # Test: get_node_at index 2
    try:
        node = ll.get_node_at(2)
        print("Value at index 2:", node.data)  # Expected: 15
    except Exception as e:
        print(e)

    # Test: delete_at index 2
    print("Delete at index 2 (removes value 15):")
    ll.delete_at(2)
    ll.print_all()  # Expected: 5 ➡ 10 ➡ 20 ➡ 30 ➡ None

    # Test: delete_last
    print("Delete last node:")
    ll.delete_last()
    ll.print_all()  # Expected: 5 ➡ 10 ➡ 20 ➡ None

    # Test: clear the list
    print("Clear the list:")
    ll.clear()
    ll.print_all()  # Expected: None 출력
